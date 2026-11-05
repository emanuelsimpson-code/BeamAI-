function execute(input) {
  // Phase 2: write the PO, the coding and the posting date to Zip, then send the bill for approval.
  // The write switch is OFF. It goes on only after the shadow run meets the bar (D3) and
  // Betterment changes Zip so that a bill posts to NetSuite only after approval (O10).
  // Endpoints: PATCH /invoices/{id}, PATCH /invoices/{id}/line_items/{lineItemId},
  //   PATCH /invoices/{id}/send_for_approval. The set-PO endpoint is to confirm (O3).
  const enabled = input.write_enabled === true || input.write_enabled === 'true';
  if (!enabled) {
    return { written: false, zip_note: 'Phase 1: the write switch is off. The proposal goes to Slack, and AP applies it in Zip.' };
  }
  return { written: false, zip_note: 'The write switch is on, but the Zip write is not built yet (Phase 2).' };
}
