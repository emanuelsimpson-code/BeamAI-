"""Shared safety helpers for talking to the BeamAI API.

- ``BeamClient`` only issues GET requests to an allow-list of read endpoints.
- ``scrub`` replaces credential-like values with ``{{SECRET:<name>}}`` placeholders.
- ``scan_pii`` reports *where* personal data appears (JSON path + kind), never the value.

Credentials come from the environment (``op run --env-file=.env.tpl -- ...``) and
are never logged, printed or written.
"""
from __future__ import annotations

import logging
import os
import re
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import requests

log = logging.getLogger("beam")

# Our workspace lives on Beam's enterprise instance (app.enterprise.beam.ai), whose API
# host is not in the public docs. Override with BEAM_BASE_URL if that changes.
BASE_URL = os.environ.get("BEAM_BASE_URL", "https://api.enterprise.beamstudio.ai").rstrip("/")
_ALLOWED_HOSTS = {"https://api.enterprise.beamstudio.ai", "https://api.beamstudio.ai"}
if BASE_URL not in _ALLOWED_HOSTS:
    raise SystemExit(f"Refusing unknown BEAM_BASE_URL: {BASE_URL}")

# Read-only endpoints we are allowed to call. Anything else is refused.
ALLOWED_GET_PATHS = [
    re.compile(r"^/agent$"),
    re.compile(r"^/agent-graphs/[A-Za-z0-9_-]+$"),
    re.compile(r"^/agent-graphs/[A-Za-z0-9_-]+/nodes/lite$"),
    re.compile(r"^/agent-graphs/[A-Za-z0-9_-]+/nodes/[A-Za-z0-9_-]+$"),
    re.compile(r"^/custom-tool/preferred-models$"),
]


class BeamClient:
    """Minimal GET-only client. Holds credentials privately; never logs them."""

    def __init__(self, timeout: float = 30.0) -> None:
        api_key = os.environ.get("BEAM_API_KEY", "")
        workspace = os.environ.get("BEAM_WORKSPACE_ID", "")
        if not api_key or not workspace:
            raise SystemExit(
                "BEAM_API_KEY / BEAM_WORKSPACE_ID not set. "
                "Run via: op run --env-file=.env.tpl -- <command>"
            )
        self._session = requests.Session()
        self._session.headers.update(
            {"x-api-key": api_key, "current-workspace-id": workspace, "accept": "application/json"}
        )
        self._timeout = timeout
        # Exact values to strip from any response text.
        self.sensitive_values: Dict[str, str] = {
            "beam_api_key": api_key,
            "beam_workspace_id": workspace,
        }

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        if not any(p.match(path) for p in ALLOWED_GET_PATHS):
            raise PermissionError(f"Refusing non-allow-listed path: {path}")
        url = BASE_URL + path
        for attempt in range(4):
            resp = self._session.get(url, params=params, timeout=self._timeout)
            if resp.status_code == 429 or resp.status_code >= 500:
                wait = 2 ** attempt
                log.warning("GET %s -> %s, retrying in %ss", path, resp.status_code, wait)
                time.sleep(wait)
                continue
            break
        if resp.status_code >= 400:
            body = self._redact_text(resp.text[:300])
            raise RuntimeError(f"GET {path} -> HTTP {resp.status_code}: {body}")
        log.info("GET %s -> %s", path, resp.status_code)
        return resp.json()

    def _redact_text(self, text: str) -> str:
        for name, value in self.sensitive_values.items():
            if value:
                text = text.replace(value, "{{SECRET:%s}}" % name)
        return text


# --------------------------------------------------------------------------- #
# Credential scrubbing
# --------------------------------------------------------------------------- #

# Keys whose values are always credentials (compared after lowercasing and removing - and _).
_SECRET_KEY_SUFFIXES = (
    "apikey", "accesstoken", "refreshtoken", "idtoken", "authtoken", "bearertoken",
    "clientsecret", "secret", "secretkey", "password", "passwd", "privatekey",
    "signingsecret", "webhooksecret", "authorization", "credential", "credentials",
    "cookie", "token", "sessiontoken", "apisecret",
)
# Keys that look secret-ish but are metadata, not secrets.
_NOT_SECRET_KEYS = {"apikeytype", "tokenusage", "tokencount", "tokens", "maxtokens", "secretname"}
# Whole subtrees that hold credentials.
_SECRET_SUBTREES = {"customauthparameters"}

_VALUE_PATTERNS: List[Tuple[str, re.Pattern]] = [
    ("stripe_secret_key", re.compile(r"\b(?:sk|rk)_(?:live|test)_[A-Za-z0-9]{10,}")),
    ("stripe_webhook_secret", re.compile(r"\bwhsec_[A-Za-z0-9]{10,}")),
    ("slack_token", re.compile(r"\bxox[abposr]-[A-Za-z0-9-]{10,}")),
    ("slack_webhook_url", re.compile(r"https://hooks\.slack\.com/services/[A-Za-z0-9/]+")),
    ("github_token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})")),
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("bearer_token", re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/=-]{16,}")),
    ("basic_auth", re.compile(r"(?i)\bbasic\s+[A-Za-z0-9+/=]{16,}")),
    ("private_key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----")),
    ("url_credentials", re.compile(r"(?<=://)[^/\s:@]+:[^/\s@]+(?=@)")),
]

_PLACEHOLDER_RE = re.compile(r"^\{\{SECRET:[a-z0-9_]+\}\}$")


def _norm(key: str) -> str:
    return key.lower().replace("-", "").replace("_", "")


def _snake(text: str) -> str:
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_") or "value"


def _is_secret_key(key: str) -> bool:
    n = _norm(key)
    if n in _NOT_SECRET_KEYS or n.endswith("type") or n.startswith("is") or n.startswith("has"):
        return False
    return any(n == s or n.endswith(s) for s in _SECRET_KEY_SUFFIXES)


@dataclass
class ScrubReport:
    placeholders: Dict[str, List[str]] = field(default_factory=dict)  # name -> json paths

    def add(self, name: str, path: str) -> str:
        self.placeholders.setdefault(name, [])
        if path not in self.placeholders[name]:
            self.placeholders[name].append(path)
        return "{{SECRET:%s}}" % name


def _context_name(ctx: List[str]) -> str:
    return ctx[-1] if ctx else "beam"


def scrub(obj: Any, report: ScrubReport, sensitive_values: Dict[str, str],
          path: str = "$", ctx: Optional[List[str]] = None, in_secret_tree: bool = False) -> Any:
    """Return a copy of ``obj`` with credentials replaced by placeholders."""
    ctx = list(ctx or [])
    if isinstance(obj, dict):
        provider = obj.get("systemIntegrationProvider") or obj.get("integrationProvider")
        if isinstance(provider, str) and provider:
            ctx = ctx + [_snake(provider)]
        out: Dict[str, Any] = {}
        for k, v in obj.items():
            p = f"{path}.{k}"
            secret_tree = in_secret_tree or _norm(k) in _SECRET_SUBTREES
            if (secret_tree or _is_secret_key(k)) and not isinstance(v, (dict, list)):
                if v in (None, "", False) or (isinstance(v, str) and _PLACEHOLDER_RE.match(v)):
                    out[k] = v
                else:
                    out[k] = report.add(f"{_context_name(ctx)}_{_snake(k)}", p)
            else:
                out[k] = scrub(v, report, sensitive_values, p, ctx, secret_tree)
        return out
    if isinstance(obj, list):
        return [scrub(v, report, sensitive_values, f"{path}[{i}]", ctx, in_secret_tree)
                for i, v in enumerate(obj)]
    if isinstance(obj, str):
        s = obj
        for name, value in sensitive_values.items():
            if value and value in s:
                s = s.replace(value, report.add(name, path))
        for kind, pat in _VALUE_PATTERNS:
            if pat.search(s):
                s = pat.sub(lambda _m, kind=kind: report.add(f"{_context_name(ctx)}_{kind}", path), s)
        return s
    return obj


# --------------------------------------------------------------------------- #
# Sample-data redaction (decision 2026-11-05: keep shape, drop values)
# --------------------------------------------------------------------------- #

SAMPLE_KEYS = {"outputexample"}


def _skeleton(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: _skeleton(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_skeleton(value[0])] if value else []
    if isinstance(value, bool):
        return "<boolean>"
    if isinstance(value, (int, float)):
        return "<number>"
    if value is None:
        return None
    return "<string>"


def shape_only(value: Any) -> Any:
    """Replace a sample value with a same-shaped skeleton of type names.

    JSON-encoded strings stay JSON-encoded strings; lists keep one element.
    """
    if isinstance(value, str):
        text = value.strip()
        if text[:1] in ("{", "["):
            try:
                import json
                return json.dumps(_skeleton(json.loads(text)), ensure_ascii=False)
            except ValueError:
                pass
        return "<string>" if value else value
    return _skeleton(value)


def redact_samples(obj: Any) -> Any:
    """Return a copy with every ``outputExample`` value reduced to its shape."""
    if isinstance(obj, dict):
        return {k: (shape_only(v) if _norm(k) in SAMPLE_KEYS else redact_samples(v)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [redact_samples(v) for v in obj]
    return obj


# --------------------------------------------------------------------------- #
# Personal-data detection (reports location + kind only)
# --------------------------------------------------------------------------- #

_EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_PHONE = re.compile(r"(?<![\w])(?:\+\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?![\w])")
_SSN = re.compile(r"(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)")
_CARD = re.compile(r"(?<!\d)(?:\d[ -]?){12,18}\d(?!\d)")
_IBAN = re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b")
_STRIPE_ID = re.compile(r"\b(?:cus|pm|card|ba|src|acct|seti)_[A-Za-z0-9]{10,}\b")
_FAKE_DOMAINS = re.compile(r"@(?:[\w-]+\.)*(?:example\.(?:com|org|net)|test|invalid|localhost|acme\.com)$", re.I)
_STRIPE_TEST_CARDS = {"4242424242424242", "4000056655665556", "5555555555554444", "378282246310005"}


def _luhn(digits: str) -> bool:
    total, alt = 0, False
    for ch in reversed(digits):
        d = int(ch)
        if alt:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        alt = not alt
    return total % 10 == 0


@dataclass
class PiiHit:
    path: str
    kind: str
    note: str = ""


_UUID = re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b")
_HEXISH = re.compile(r"\b(?=[0-9a-fA-F]*[a-fA-F])(?=[0-9a-fA-F]*\d)[0-9a-fA-F]{16,}\b")
_EPOCH_MS = re.compile(r"(?<!\d)1[5-9]\d{11}(?!\d)")
# Numeric object IDs written as `id: 123...` / `"id": 123...` (e.g. Zendesk custom-field IDs).
_ID_VALUE = re.compile(r"(\b[\w]*id[\"']?\s*:\s*)\d{10,19}\b", re.I)
INTERNAL_EMAIL_DOMAINS = ("betterment.com",)


def _email_bucket(addr: str) -> str:
    domain = addr.rsplit("@", 1)[-1].lower()
    if _FAKE_DOMAINS.search(addr):
        return "example/test domain"
    if any(domain == d or domain.endswith("." + d) for d in INTERNAL_EMAIL_DOMAINS):
        return "internal domain"
    return "other domain"


_ID_PARAM_NAME = re.compile(r"id$", re.I)  # e.g. ticket.ticket_form_id, group_id, brandId


def scan_pii(obj: Any, path: str = "$", numeric_ok: bool = False) -> List[PiiHit]:
    """``numeric_ok``: the string is the static value of an ID parameter, so long
    digit runs are object IDs (e.g. Zendesk form IDs), not cards or phones."""
    hits: List[PiiHit] = []
    if isinstance(obj, dict):
        id_param = isinstance(obj.get("paramName"), str) and bool(_ID_PARAM_NAME.search(obj["paramName"]))
        for k, v in obj.items():
            hits += scan_pii(v, f"{path}.{k}", numeric_ok=id_param and k == "staticValue")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += scan_pii(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        for m in _EMAIL.finditer(obj):
            hits.append(PiiHit(path, "email", _email_bucket(m.group())))
        # Remove UUIDs, hex IDs and epoch-millisecond timestamps before numeric checks.
        numeric = _ID_VALUE.sub(r"\1 ", _EPOCH_MS.sub(" ", _HEXISH.sub(" ", _UUID.sub(" ", obj))))
        if numeric_ok and re.fullmatch(r"\s*\d{1,19}\s*", obj):
            numeric = ""
        if _PHONE.search(numeric):
            hits.append(PiiHit(path, "phone_number"))
        if _SSN.search(numeric):
            hits.append(PiiHit(path, "ssn_like"))
        for m in _CARD.finditer(numeric):
            digits = re.sub(r"\D", "", m.group())
            if 13 <= len(digits) <= 19 and _luhn(digits):
                grouped = bool(re.search(r"[ -]", m.group()))
                note = "Stripe published test card" if digits in _STRIPE_TEST_CARDS else (
                    "passes Luhn, card-style grouping" if grouped else "passes Luhn, plain digit run")
                hits.append(PiiHit(path, "payment_card", note))
        if _IBAN.search(numeric):
            hits.append(PiiHit(path, "iban_like"))
        if _STRIPE_ID.search(obj):
            hits.append(PiiHit(path, "stripe_customer_or_payment_id"))
    return hits
