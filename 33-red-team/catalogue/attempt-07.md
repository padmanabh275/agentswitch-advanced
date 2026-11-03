# Attempt 07

## Attempt
Read another seat’s skills and tasks.

## Boundary
Agent records — skills/tasks of other seats are readable; email still must not leak.

## Steps
1. Pick a foreign seat id from Attempt 06 (not seat 33).
2. Call skill list/read and task list/read for that seat.
3. Confirm payloads are agent metadata only (no mailbox contents).

## Expected
Read allowed for skills and tasks of the other seat.

## Actual
AgentSkill.list{}->ok {"data": [{"id": "<uuid>", "company_id": "<uuid>", "name": "Purchasing Skill", "agent_persona_id": "<uuid>", "version": 1.0, "supersedes_id": null, "summary": " | AgentTask.list{}->ok {"data": [{"id": "<uuid>", "number": "AT-2026-00104", "name": "[seat23] Chase overdue checklists and unowned runs", "description": "Recorded by the checklist agent ([checklist_agent]). Paused until a person activates it. | AgentSkill.list{'seat_number': 6}->rpc_error code=i


## Result
Held

