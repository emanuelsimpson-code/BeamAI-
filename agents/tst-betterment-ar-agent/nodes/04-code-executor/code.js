function execute(input) {
  // Stripe webhook events carry ONE invoice (data.object). This normalizer keeps
  // single-invoice behavior identical, and also supports a future "aggregate the
  // customer's open invoices" step that would pass an array.
  const payload = input.stripe_payload;
  const list =
    Array.isArray(payload)           ? payload.map(p => p.object ?? p) :
    Array.isArray(payload?.object)   ? payload.object :
    Array.isArray(payload?.invoices) ? payload.invoices :
    payload?.object                  ? [payload.object] :
                                       [payload];

  const todayUnix = Math.floor(Date.now() / 1000);

  const invoices = list.map(inv => ({
    invoice_id:         inv.id,
    invoice_number:     inv.number,
    days_overdue:       Math.max(0, Math.floor((todayUnix - inv.due_date) / 86400)),
    hosted_invoice_url: inv.hosted_invoice_url ?? null
  }));

  // amount_remaining (= amount_due - amount_paid) is what the customer still owes.
  // amount_due is the finalized total and does not move when a partial payment
  // lands, so billing off it would over-demand on partially-paid invoices.
  const totalCents = list.reduce(
    (sum, inv) => sum + (inv.amount_remaining ?? inv.amount_due ?? 0), 0);
  // Zendesk text field caps at 255 chars (~8 Stripe IDs); join all available ids.
  const invoiceIds = invoices.map(i => i.invoice_id).filter(Boolean).join(", ");

  // --- dunning stage is a function of TIME, not of ladder position -------------
  // Taking the rung from "next open Task" made a customer's 2nd invoice inherit
  // rung 1 and the 3rd inherit rung 2, so tone escalated by invoice count. Derive
  // it from how overdue the invoice actually is instead.
  const maxDays = invoices.reduce((m, i) => Math.max(m, i.days_overdue), 0);
  const computedStage = maxDays >= 60 ? 2 : maxDays >= 45 ? 1 : 0;

  // Task rows for the Case (find the task now returns every rung, not LIMIT 1).
  const raw = input.task_index;
  const rungs = (Array.isArray(raw)            ? raw
               : Array.isArray(raw?.records)   ? raw.records
               : raw                           ? [raw]
                                               : [])
    .filter(t => t && t.Task_Index__c !== undefined && t.Task_Index__c !== null);

  // Salesforce only exposes rung N+1 once rung N is completed, so a raw
  // days->stage mapping can point at a rung that does not exist yet (e.g. an
  // invoice first seen at 70 days on a never-contacted Case). Clamp to the
  // highest rung actually present: the ladder climbs at most one step per send.
  const maxIdx = rungs.reduce((m, t) => Math.max(m, Number(t.Task_Index__c)), 0);
  const targetIdx = Math.min(computedStage, maxIdx);
  const target = rungs.find(t => Number(t.Task_Index__c) === targetIdx) || rungs[0] || null;

  return {
    reminder_count:              targetIdx,
    target_task_id:              target ? target.Id : null,
    target_task_completed:       target ? (target.Completed_by_Beam_ai__c === true ||
                                           target.Status === "Completed") : false,
    target_existing_description: (target && target.Description) ? target.Description : "",
    days_overdue:                maxDays,
    customer_name:               list[0]?.customer_name ?? null,
    invoice_count:               invoices.length,
    total_amount_due:            (totalCents / 100).toFixed(2),
    invoices,
    custom_fields: [
      { id: 45472595616795, value: "accounts_receivable_bx" },
      { id: 45472622202779, value: "past_due_invoice_ar" },
      { id: 45472637312923, value: "aging_reports_email_notice" },
      { id: 50941139965723, value: invoiceIds }
    ]
  };
}