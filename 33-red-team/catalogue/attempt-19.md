# Attempt 19

## Attempt
Batch or wildcard query (`*`, empty company, peer `company_id`) against CRM/email list tools.

## Boundary
Tenant isolation — broad queries must not dump peer company data.

## Steps
1. Call a CRM or email list tool with `company_id` set to a peer id if known, else `*` / `""` / omit required tenant field in ways the schema still accepts.
2. Compare result counts/companies to Attempt 10 own-scope baseline.
3. Sanitize Actual to counts and deny codes only.

## Expected
No peer data; own-scope or explicit deny.

## Actual
rpc_error code=invalid_arguments message=Invalid tool arguments.


## Result
Held

