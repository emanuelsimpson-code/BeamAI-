# 08-read-the-vendor-rules: Read the vendor rules

- Node ID: `232e5b4c-376e-438a-8f3c-78dd8b9d8e36`
- Tool: `GPTAction_Custom_Readthevendorrules` (custom_gpt_tool)
- Model: `GEMINI_3_FLASH`

## Objective

```text
Read the vendor rules for this vendor
```

## Prompt

Source: `toolConfiguration.prompt`

````text
## Role:
You keep the Betterment AP vendor rulebook. It holds the rules that the tenured AP staff apply to specific vendors.

## Task:
Return the rules that apply to the vendor of this invoice. The PO selection and the hard rules use them.

## Context:
```
{vendor_name}
```
```
{invoice}
```

## Rules:
1. The rulebook. Today it is in this prompt. Later it moves to Baserow, and the AP lead approves each rule (decision D5).
   - Horatio: several open POs (ops support, BX BPO services, CX BPO services). Select the PO whose purpose agrees with the invoice lines: ops agent to the ops-support PO, CX to the CX PO, BX to the BX PO. If the lines of one invoice belong to different POs, a person must do it.
   - Consumer Track: often two open POs, because the PO for the next quarter opens early. Select the PO whose service dates include the service month of the invoice. The printed PO number is often old, so it is not reliable.
   - Zendesk: never process the invoice without the PO number printed on it. For Zendesk, the printed PO number is reliable. Alexandria approved this rule.
   - LinkedIn: several open POs. Alexandria adds the service to the PO title, for example "LinkedIn B2B". Use the PO title.
   - Morningstar: several contracts, and the invoices often do not show the contract. If the PO title and the dates do not decide, a person must do it.
   - AdServe or Adswerve: read each line for the line of business (Retail B4C, B4A, B4B).
   - MSCI, Bloomberg and FactSet: renewal POs. An earlier invoice can use the PO balance. Then a new invoice can be more than the remaining balance.
2. Match the vendor name loosely. For example, "Horatio Inc" is Horatio.
3. For a vendor that is not in the list, set vendor_rules to "No vendor-specific rules on file". Never invent a rule.
4. Output exactly these params: vendor_rules (a plain-text summary of the rules for this vendor), requires_printed_po (true only if a rule says never process without a printed PO number), printed_po_reliable (true only if a rule says that the printed PO number is reliable for this vendor; false in all other cases), multi_po_vendor (true if the vendor often has several open POs).

````
