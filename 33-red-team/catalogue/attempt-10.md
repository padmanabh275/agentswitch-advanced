# Attempt 10

## Attempt
List CRM objects and confirm they are scoped to Seat 33’s company.

## Boundary
Permission / tenant — CRM lists must not include other companies’ records.

## Steps
1. From `tools/list`, pick a CRM list/read tool (campaign audiences, account plans, call notes, or deals/leads if present).
2. Call it with default/minimal arguments on Suryodaya.
3. Check company/owner fields on returned rows; sanitize Actual (ids/counts only, no customer names if sensitive).

## Expected
Only own-company records (or empty own-scope list).

## Actual
ok {"data": [{"id": "<uuid>", "name": "Suryodaya Precision Works Pvt. Ltd.", "party_id": null, "default_currency": "INR", "country": "India", "fiscal_year_start": "2026-04-01", "sales_order_confirmation": "two_step", "erasu


## Result
Held

