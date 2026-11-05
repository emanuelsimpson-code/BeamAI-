function execute(input) {
  // The vendor has exactly one open PO. Code checks it. No LLM.
  // The hard rules (later step) send the invoice to a person when a check fails.
  const parse = v => { if (typeof v !== 'string') return v; try { return JSON.parse(v); } catch (e) { return null; } };
  const norm = s => String(s || '').toLowerCase().replace(/[^a-z0-9]/g, '').replace(/^po/, '');
  const subName = s => String((s && typeof s === 'object') ? (s.name || s.id || '') : (s || ''));
  const inv = parse(input.invoice) || {};
  const pos = parse(input.open_pos);
  const po = (Array.isArray(pos) && pos[0]) || {};
  const lines = Array.isArray(inv.line_items) ? inv.line_items : [];
  const subtotal = inv.subtotal != null ? Number(inv.subtotal)
    : inv.amount != null ? Number(inv.amount) - Number(inv.tax || 0)
    : lines.reduce((a, l) => a + Number(l.amount || 0), 0);
  const remaining = po.remaining != null ? Number(po.remaining)
    : Number(po.total_amount || 0) - Number(po.amount_billed || 0) + Number(po.amount_credited || 0);
  const reliable = input.printed_po_reliable === true || input.printed_po_reliable === 'true';
  const failed = [];
  let confidence = 0.97;
  const invSub = String(input.subsidiary || inv.subsidiary || '');
  const poSub = subName(po.subsidiary);
  if (invSub && poSub && norm(invSub) !== norm(poSub)) { failed.push('S5: the PO subsidiary is not the invoice subsidiary'); confidence = Math.min(confidence, 0.2); }
  if (inv.service_start && po.start_date && po.end_date &&
      (inv.service_start < po.start_date || (inv.service_end || inv.service_start) > po.end_date)) {
    failed.push('S3: the service period is outside the PO dates'); confidence = Math.min(confidence, 0.3);
  }
  if ((po.remaining != null || po.total_amount != null) && remaining < subtotal) {
    failed.push('S6: the remaining balance (' + remaining + ') is less than the invoice amount (' + subtotal + ')'); confidence = Math.min(confidence, 0.4);
  }
  if (reliable && input.printed_po_number && norm(input.printed_po_number) !== norm(po.po_number)) {
    failed.push('S1: the printed PO number points to a different PO'); confidence = Math.min(confidence, 0.3);
  }
  const selected = String(po.po_number || po.id || '');
  return {
    decision: {
      path: 'po_backed',
      method: 'one_open_po',
      selected_po: selected,
      selected_po_id: String(po.id || ''),
      second_best_po: '',
      scores: [{ po: selected, score: confidence, reasons: failed.length ? failed.join('; ') : 'All checks pass' }],
      confidence: confidence,
      needs_more_than_one_po: false,
      line_map: [],
      reasoning: failed.length
        ? 'The vendor has one open PO, but a check failed: ' + failed.join('; ') + '.'
        : 'The vendor has one open PO. The subsidiary, the dates, the balance and the printed PO number agree.'
    }
  };
}
