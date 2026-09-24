---
name: coordinate-codex-tasks
description: Handle an explicit request to delegate work to a separate Codex Task. When the current Task remains the coordinator, create and maintain one dedicated heartbeat per executing Task, track meaningful progress, and close each monitor after verification. Do not invoke for ordinary subagents.
---

# Coordinate Codex Tasks

Use this skill whenever the user explicitly asks to create or continue another **Codex Task**, including when they do not say whether the current Task should monitor it. A skill guides the model's choices; it is not an automatic hook on every Task creation.

The **coordinating Task** uses this skill. Give an executing Task its objective, scope, and acceptance evidence; do not ask it to load this coordination skill or manage its own monitor unless the user separately makes it a coordinator.

## Decide who owns follow-through

- If the user wants a separate, user-owned Task to pursue its own objective, dispatch it and make its location clear. Check that it started, then let the user follow it there. Do not add a monitor for that independent Task.
- If the user delegates part of the current Task's assignment to the new Task, the current Task remains the coordinator and owns final integration and verification unless the user explicitly transfers that responsibility. Create a **new, dedicated monitor for this executing Task** once its real `threadId` is available. This applies even if the user did not separately say "monitor."
- Keep a one-to-one mapping between executing Task ID and monitor ID. Do not put several executing Tasks in one heartbeat or repurpose another Task's monitor. If this executing Task already has its monitor, update that monitor rather than creating a duplicate.
- Respect an explicit request to leave monitoring to the new Task, avoid scheduling, or stop at dispatch. If ownership is genuinely unclear and would change external actions, ask while completing the independent dispatch work.

## Start with the actual assignment

- Create a separate Task only when the user explicitly requests one. For an internal subtask, use the available subagent mechanism instead. If the requested Task already exists, continue it rather than creating a duplicate.
- Give the executing Task a concrete objective, scope, owner, acceptance evidence, and any existing IDs or checkpoints. Keep the coordinator's responsibilities explicit. Follow `create_thread` project and environment rules, and wait for a real `threadId` before using tools that require one.
- Check the executing Task's initial status before treating dispatch as successful. When this Task owns follow-through, read its first progress and the relevant source of truth; `completed` or `idle` alone does not prove the assignment is complete.

## Give each delegated Task its own heartbeat

- Use `automation_update` to create a heartbeat targeted at the **coordinating Task's `threadId`**, with a distinct name and automation ID for this executing Task. The coordinating Task may have several heartbeats, each monitoring one executing Task. Record the coordinator, executing Task, and monitor IDs; read back the new monitor's target and `ACTIVE` status, and confirm existing monitors were not replaced. Do not substitute a standalone cron automation unless the user explicitly requests that form.
- Choose a cadence that matches the executing work. Start around 15 minutes for ordinary long-running work and lengthen it for slow stages; do not use minute-by-minute polling merely to show progress or test a scheduler. While the coordinator is actively waiting, use `wait_threads` instead of increasing heartbeat frequency.
- The monitor prompt names exactly one executing Task, its objective, current verified checkpoint, next evidence to inspect, boundaries, and completion or stop condition. On wake, the coordinator reads that Task and actual artifact state before acting. It must avoid restarting or duplicating work already active in the executing Task, and stay quiet when nothing material changes.
- On a meaningful stage change, blocker, required decision, or result, the coordinator updates only that executing Task's monitor and sends a scoped correction to the executing Task when needed. Avoid status messages or prompt rewrites at every poll; they impose communication cost and may interrupt the executing Task. Use `wait_threads` while the coordinator's turn is active and independently check consequential results. A monitor prompt is a handoff checkpoint, not current-state authority.
- Apply the same state rules on scheduled wakes and live checks:
  - `active`, no verified change: leave the heartbeat `ACTIVE` and its prompt unchanged; send no message.
  - New verified stage or recoverable blocker: keep `ACTIVE`, update only this heartbeat's checkpoint and next check; send the executing Task one specific correction only if action is needed.
  - `idle` or turn `completed` while the assignment remains unfinished: inspect the final message and real artifacts, then resume the same Task with a scoped instruction when authorized. Keep `ACTIVE` only while useful work can continue.
  - Outcome verified complete, or a terminal blocker or required user decision: set only this heartbeat to `PAUSED`, read back its saved status, and report the result or blocker once.
- Preserve the existing cadence and other saved fields when changing a heartbeat's prompt or status. A Task status is a signal to inspect; it never substitutes for the assignment's completion evidence.
- If the tool rejects a distinct heartbeat on the coordinator, do not silently merge assignments into one monitor or overwrite another monitor. Continue available live supervision and report the concrete platform limitation. Do not infer permission for a new objective or irreversible action from the existence of a heartbeat.

## Close the loop

- Verify the requested outcome with the evidence appropriate to that task. Distinguish child Task completion, deliverable completion, and any external release or read-back gates.
- Pause that executing Task's dedicated heartbeat when the coordinator verifies the objective complete, or when a terminal blocker or required user decision makes further scheduled work inappropriate. Read back the saved status. Report the result or exact blocker and any remaining work once, without recurring unchanged updates.

Use the current Codex tool schemas for `create_thread`, `wait_threads`, `read_thread`, `send_message_to_thread`, and `automation_update`. Do not edit automation files by hand.
