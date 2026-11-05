function execute(input) {
  // The classifier found an item that is not an invoice (high confidence).
  // Phase 1: post a note only. Phase 2: archive the item in Zip.
  // TODO (O3): Zip documents no archive endpoint. Ask the Zip contact before the write.
  const preview = String(input.document_text || '').replace(/\s+/g, ' ').slice(0, 90);
  const link = input.zip_url ? ' | <' + input.zip_url + '|Open in Zip>' : '';
  return {
    archived: false,
    archive_note: [
      '*Not an invoice: archive recommended*',
      'Item: ' + (input.vendor_name || 'unknown sender') + ' (' + (input.invoice_id || 'no id') + ')' + link,
      'Reason: ' + (input.reason || 'n/a'),
      'Preview: "' + preview + '..."',
      'Action: archive the item in the Zip Inbox. An archive is a soft delete. To undo it, restore the item from the archived items in Zip.',
      'The agent did not change Zip. Zip writes start in Phase 2.'
    ].join('\n')
  };
}
