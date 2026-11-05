function execute(input) {
  // Confidence gate. The agent proceeds only when no hard rule hit and the confidence is at or
  // above the threshold. Betterment can change the threshold (decision D6, start value 0.90).
  const parse = v => {
    if (v === null || v === undefined || v === '') return null;
    if (typeof v !== 'string') return v;
    try { return JSON.parse(v); } catch (e) { return null; }
  };
  const threshold = Number(input.confidence_threshold || 0.9);
  const d = parse(input.decision) || {};
  const bill = parse(input.bill) || {};
  const inv = parse(input.invoice) || {};
  const conf = Number(d.confidence || 0);
  const hardHit = input.hard_rule_hit === true || input.hard_rule_hit === 'true';
  const proceed = !hardHit && conf >= threshold;
  const scoreOf = po => {
    const s = (Array.isArray(d.scores) ? d.scores : []).find(x => x && x.po === po);
    return s && s.score != null ? ' (score ' + Number(s.score).toFixed(2) + ')' : '';
  };
  const lines = Array.isArray(bill.lines) ? bill.lines : [];
  const msg = [
    proceed ? '*Proposal: PO match ready for AP*' : '*Needs a person: the agent does not guess*',
    'Vendor: ' + (input.vendor_name || 'unknown') + ' | Invoice: ' + (inv.invoice_number || inv.id || 'n/a') +
      (inv.amount != null ? ' | Amount: ' + inv.amount + (inv.currency ? ' ' + inv.currency : '') : ''),
    input.zip_url ? 'Zip: <' + input.zip_url + '|Open the invoice in Zip>' : 'Zip: link not available',
    'Route: PO-backed, ' + (d.method === 'several_open_pos' ? 'several open POs (scored)' : 'one open PO (checked)'),
    'Selected PO: ' + (d.selected_po || 'none') + scoreOf(d.selected_po) +
      (d.second_best_po ? ' | Second-best PO: ' + d.second_best_po + scoreOf(d.second_best_po) : ''),
    'Confidence: ' + conf.toFixed(2) + ' (threshold ' + threshold.toFixed(2) + ')',
    'Posting date: ' + (input.posting_date || 'none') + (input.posting_rule ? ' (' + input.posting_rule + ')' : '')
  ];
  if (lines.length) {
    msg.push('Bill lines: ' + lines.map(l => l.amount + ' to GL ' + (l.gl_account || '?') + ', ' + (l.department || '?') +
      (l.line_of_business ? ', ' + l.line_of_business : '')).join(' | '));
  }
  if (hardHit) msg.push('Hard rules: ' + input.hard_rule_reasons);
  msg.push('Reasons: ' + (d.reasoning || 'n/a'));
  msg.push(proceed
    ? 'Action: check the proposal, then link the PO and create the bill in Zip.'
    : 'Action: select the correct PO in Zip, or reject the invoice and ask for the correct PO.');
  return {
    route: proceed ? 'proceed' : 'human',
    route_reason: hardHit ? 'hard rule: ' + input.hard_rule_reasons
      : (proceed ? 'confidence at or above the threshold' : 'confidence below the threshold'),
    slack_message: msg.join('\n')
  };
}
