function execute(input) {
  // Reads the open POs of the vendor and the request history from Zip.
  // TODO (needs the Zip key and docs, O2 and O3):
  //   GET /purchase_orders?vendor_id={vendor_id} with the open status, then GET /purchase_orders/{id}.
  //   Keep for each PO: id, po_number, title, start_date, end_date, total_amount, amount_billed,
  //   amount_credited, remaining (total - billed + credited), subsidiary, department, requester,
  //   line_items (id, description, amount, gl_account, department, location, line_of_business).
  //   requester_history: GET /requests for this vendor and the original request of each PO.
  //   zip_suggested_po: the Zip auto-match, if the invoice record shows it (O3). Low trust (S8).
  // TEST ONLY: draft tasks send invoice.test_open_pos, invoice.test_requester_history and
  //   invoice.test_zip_suggested_po. Remove this before go-live.
  const parse = v => { if (typeof v !== 'string') return v; try { return JSON.parse(v); } catch (e) { return null; } };
  const inv = parse(input.invoice) || {};
  const openPos = Array.isArray(inv.test_open_pos) ? inv.test_open_pos : [];
  const history = Array.isArray(inv.test_requester_history) ? inv.test_requester_history : [];
  return {
    open_pos: openPos,
    po_count: openPos.length,
    requester_history: history,
    zip_suggested_po: String(inv.test_zip_suggested_po || '')
  };
}
