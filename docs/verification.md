# Verification record

## Observed locally, 2026-09-25 (Asia/Taipei)

- Two separate GPT-6 Luna Tasks were created for bounded read-only work. Their session metadata identified the requested model, and both Tasks completed.
- Two different heartbeat automations were simultaneously `ACTIVE` and targeted the same coordinating Task. Each prompt named only its own delegated Task.
- Updating the first heartbeat left the second one's saved prompt and update timestamp unchanged.
- Pausing the first heartbeat left the second `ACTIVE`; the second was then paused independently. Both saved statuses were read back as `PAUSED`.
- An initially one-minute experimental cadence was changed to 15 minutes after user feedback. The executing Tasks were told to finish without waiting for the schedule.
- The coordinator-only skill was validated with Codex skill-creator `quick_validate.py`.

The 15-minute interval above records the experiment; it is not a current default. The current skill lets the coordinator choose and adjust intervals up to a 30-minute maximum. This ceiling expresses the user's cache-related preference; it is not a verified cache-retention guarantee.

## Not established by that experiment

- The heartbeats did **not** complete a timed wake-and-react cycle. Autonomous status-based prompt changes and self-pausing after a scheduled wake remain unverified.
- The skill is a set of instructions, not a native event hook. Model selection and tool availability can affect whether it is applied.

## Identity wording checks, 2026-10-01 (Asia/Taipei)

The first role-question experiment **announced itself as a test**, which may have prompted extra attention to identity:

| Model and message | Observed response |
| --- | --- |
| GPT-6.1 Sol, old “本 Task 是主程” | Identified itself as the worker, but said “本 Task” could refer to sender or recipient; ownership was not fully certain. |
| Same Sol Task, explicit sender/recipient roles and Task IDs | Identified the worker and coordinator responsibilities and reported no role ambiguity. |
| Fresh GPT-6 Luna, old “本 Task 是主程” | Identified itself as the worker and flagged the phrase as ambiguous. |

A separate fresh **GPT-6 Luna** Task then received ordinary read-only work messages without calling them tests. Its first message used the old “本 Task” wording for an English README link audit; its second message explicitly named both Task IDs and responsibilities for a matching Traditional Chinese README link audit. It completed both audits, reporting 10 existing local targets in each README, made no edits, and suggested a README maintainer for any later synchronization check. It did not visibly claim coordinator or monitor ownership in either turn.

The natural-work comparison found no role mistake in the old-message turn, so it cannot establish that the revised wording reduced an observed failure rate. The second turn also inherited the first turn's context. These observations support keeping the role mapping explicit while leaving broader behavior and scheduled-wake reliability unproven. Model identities were read from each Task's local turn metadata.

The repository check (`python3 scripts/check.py`) verifies the published package's basic structure and image constraints. It does not change these runtime limits.
