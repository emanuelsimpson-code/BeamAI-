function execute(input) {
  // Hard rules H1 to H8. A hard rule always sends the invoice to a person, at any confidence.
  // H9 (invoice on hold or with an alert in Zip) is in the intake agent: it creates no task.
  const parse = v => {
    if (v === null || v === undefined || v === '') return null;
    if (typeof v !== 'string') return v;
    try { return JSON.parse(v); } catch (e) { return null; }
  };
  const yes = v => v === true || v === 'true';
  const norm = s => String(s || '').toLowerCase().replace(/[^a-z0-9]/g, '').replace(/^po/, '');
  const subName = s => String((s && typeof s === 'object') ? (s.name || s.id || '') : (s || ''));
  const d = parse(input.decision) || {};
  const bill = parse(input.bill) || {};
  const inv = parse(input.invoice) || {};
  const posList = parse(input.open_pos);
  const pos = Array.isArray(posList) ? posList : [];
  const tolerance = Number(input.tolerance || 0);
  const po = pos.find(p => (d.selected_po_id && String(p.id) === String(d.selected_po_id)) ||
                           norm(p.po_number) === norm(d.selected_po)) || null;
  const hits = [];
  const add = (id, text) => hits.push({ id: id, text: id + ': ' + text });

  if (!input.invoice_id || !input.vendor_id) add('H7', 'the payload is not complete, or the vendor is not in Zip. Check the fraud signals');
  if (yes(input.requires_printed_po) && !input.printed_po_number) add('H1', (input.vendor_name || 'The vendor') + ' needs a printed PO number, and the invoice has none');
  if (!po) {
    add('H7', 'no PO was selected, or the selected PO is not an open PO of the vendor');
  } else {
    const invSub = String(input.subsidiary || inv.subsidiary || '');
    const poSub = subName(po.subsidiary);
    if (invSub && poSub && norm(invSub) !== norm(poSub)) add('H2', 'the PO is for ' + poSub + ', and the invoice is for ' + invSub);
    const remaining = po.remaining != null ? Number(po.remaining)
      : Number(po.total_amount || 0) - Number(po.amount_billed || 0) + Number(po.amount_credited || 0);
    const amount = Number(bill.subtotal != null ? bill.subtotal : (inv.amount || 0));
    if ((po.remaining != null || po.total_amount != null) && remaining + tolerance < amount) {
      add('H3', 'the remaining balance on the PO (' + remaining + ') is less than the invoice amount (' + amount + ')');
    }
    if (inv.service_start && po.start_date && po.end_date &&
        (inv.service_start < po.start_date || (inv.service_end || inv.service_start) > po.end_date)) {
      add('H5', 'the service period (' + inv.service_start + ' to ' + (inv.service_end || inv.service_start) +
        ') is outside the PO dates (' + po.start_date + ' to ' + po.end_date + '). Reject the invoice and ask for the correct PO');
    }
    if (yes(input.printed_po_reliable) && input.printed_po_number && norm(input.printed_po_number) !== norm(po.po_number)) {
      add('H8', 'the printed PO number (' + input.printed_po_number + ') is reliable for this vendor and points to a different PO');
    }
  }
  if (yes(d.needs_more_than_one_po)) add('H4', 'the invoice lines need more than one PO. Zip links one invoice to one PO only');
  if (yes(input.prepaid_candidate)) add('H6', 'the invoice is a prepaid candidate (rule P4). A person does a prepaid review');
  if (input.unmapped_lines) add('Lines', 'a line does not map to a PO line: ' + input.unmapped_lines);

  return {
    hard_rule_hit: hits.length > 0,
    hard_rules_hit: hits.map(h => h.id).join(', '),
    hard_rule_reasons: hits.map(h => h.text).join('; ')
  };
}
