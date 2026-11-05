function execute(input) {
  // Prepares the bill for the selected PO: posting date (rules P1 to P4), lines and coding.
  // Code calculates the posting date, not the LLM. The coding always comes from the PO line.
  const parse = v => {
    if (v === null || v === undefined || v === '') return null;
    if (typeof v !== 'string') return v;
    try { return JSON.parse(v); } catch (e) { return null; }
  };
  const norm = s => String(s || '').toLowerCase().replace(/[^a-z0-9]/g, '').replace(/^po/, '');
  const round2 = n => Math.round(Number(n || 0) * 100) / 100;
  const iso = d => d.toISOString().slice(0, 10);
  const day = s => new Date(String(s).slice(0, 10) + 'T00:00:00Z');

  // Only one of the two PO selection steps ran. Take the result that is there.
  const decision = [input.decision_multi, input.decision_single].map(parse)
    .find(d => d && typeof d === 'object' && d.path === 'po_backed') || null;
  const inv = parse(input.invoice) || {};
  const posList = parse(input.open_pos);
  const pos = Array.isArray(posList) ? posList : [];
  const holidays = (parse(input.holidays) || []).map(String);
  const prepaidMin = Number(input.prepaid_threshold || 10000);

  if (!decision) {
    return {
      decision: { path: 'unknown', confidence: 0, reasoning: 'No PO selection result' },
      bill: {}, posting_date: '', posting_rule: 'No bill: no PO selection result',
      prepaid_candidate: false, unmapped_lines: '', bill_summary: 'No bill: no PO selection result'
    };
  }
  const po = pos.find(p => (decision.selected_po_id && String(p.id) === String(decision.selected_po_id)) ||
                           norm(p.po_number) === norm(decision.selected_po)) || null;

  // Posting date. AP closes on business day 4. Business days exclude weekends and the holidays.
  // TEST ONLY: invoice.test_processing_date sets the processing date in draft tasks.
  const today = inv.test_processing_date ? day(inv.test_processing_date) : day(new Date().toISOString());
  const isBiz = d => { const w = d.getUTCDay(); return w !== 0 && w !== 6 && !holidays.includes(iso(d)); };
  let bizDay = 0;
  for (const x = new Date(Date.UTC(today.getUTCFullYear(), today.getUTCMonth(), 1)); x <= today; x.setUTCDate(x.getUTCDate() + 1)) {
    if (isBiz(x)) bizDay++;
  }
  let postingDate, rule;
  if (bizDay <= 4) {
    postingDate = iso(new Date(Date.UTC(today.getUTCFullYear(), today.getUTCMonth(), 0)));
    rule = 'P1: processed on business day ' + bizDay + ', so the last day of the previous month';
  } else {
    postingDate = iso(today);
    rule = 'P2: processed on business day ' + bizDay + ', so the processing date (default, to confirm)';
  }
  const svcStart = inv.service_start ? day(inv.service_start) : null;
  const svcEnd = inv.service_end ? day(inv.service_end) : null;
  if (svcStart && iso(svcStart).slice(0, 7) > postingDate.slice(0, 7)) {
    postingDate = iso(svcStart).slice(0, 7) + '-01';
    rule = 'P3: the service starts in a later month, so the first day of the service month (GL team to confirm)';
  }
  const total = inv.amount != null ? Number(inv.amount) : 0;
  const longService = svcStart && svcEnd && (svcEnd - svcStart) / 86400000 > 31;
  let prepaid = false;
  if (total >= prepaidMin && longService) {
    prepaid = true;
    postingDate = '';
    rule = 'P4: total of ' + total + ' and a service period longer than one month, so no date. A person does a prepaid review.';
  }

  // Lines and coding from the PO.
  const invLines = (Array.isArray(inv.line_items) ? inv.line_items : [])
    .filter(l => !/\btax\b/i.test(String(l.description || '')));
  const subtotal = inv.subtotal != null ? Number(inv.subtotal)
    : inv.amount != null ? Number(inv.amount) - Number(inv.tax || 0)
    : invLines.reduce((a, l) => a + Number(l.amount || 0), 0);
  const poLines = po && Array.isArray(po.line_items) ? po.line_items : [];
  const coding = l => ({
    gl_account: String(l.gl_account || ''), department: String(l.department || ''),
    location: String(l.location || ''), line_of_business: String(l.line_of_business || '')
  });
  const words = s => String(s || '').toLowerCase().split(/[^a-z0-9]+/).filter(w => w.length > 1);
  const bestLine = desc => {
    const w = words(desc);
    if (!w.length) return null;
    const scored = poLines.map(p => ({ p, s: w.filter(x => words(p.description).includes(x)).length / w.length }))
      .sort((a, b) => b.s - a.s);
    if (!scored.length || scored[0].s < 0.5) return null;
    if (scored[1] && scored[1].s === scored[0].s) return null;
    return scored[0].p;
  };

  let lines = [];
  const unmapped = [];
  if (!po) {
    unmapped.push('the selected PO is not in the open POs of the vendor');
  } else if (poLines.length <= 1) {
    const src = poLines[0] || po;
    lines = [Object.assign({
      description: (po.title || po.po_number || 'Invoice') + (inv.service_start ? ' (service ' + inv.service_start + ')' : ''),
      amount: round2(subtotal),
      po_line: String((poLines[0] && (poLines[0].id || poLines[0].description)) || '')
    }, coding(src))];
  } else {
    const map = Array.isArray(decision.line_map) ? decision.line_map : [];
    const groups = {};
    invLines.forEach((l, i) => {
      const m = map.find(x => Number(x.invoice_line) === i);
      let target = m ? poLines.find(p => String(p.id) === String(m.po_line) || p.description === m.po_line) : null;
      if (!target) target = bestLine(l.description);
      if (!target) { unmapped.push(String(l.description || 'line ' + (i + 1))); return; }
      const key = String(target.id || target.description);
      if (!groups[key]) groups[key] = Object.assign({ description: String(target.description || ''), amount: 0, po_line: key }, coding(target));
      groups[key].amount = round2(groups[key].amount + Number(l.amount || 0));
    });
    lines = Object.values(groups);
  }

  const bill = {
    po: decision.selected_po, po_id: po ? String(po.id || '') : '',
    posting_date: postingDate, posting_rule: rule, business_day: bizDay,
    subtotal: round2(subtotal), lines: lines
  };
  const summary = 'Bill for ' + decision.selected_po + ': posting date ' + (postingDate || 'none') + ' (' + rule.split(':')[0] + '), ' +
    lines.length + ' line(s): ' + lines.map(l => l.amount + ' to GL ' + (l.gl_account || '?') + ' / ' + (l.department || '?') +
    (l.line_of_business ? ' / ' + l.line_of_business : '')).join('; ');
  return {
    decision: decision, bill: bill, posting_date: postingDate, posting_rule: rule,
    prepaid_candidate: prepaid, unmapped_lines: unmapped.join('; '), bill_summary: summary
  };
}
