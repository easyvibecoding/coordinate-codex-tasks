# Verification record

## Observed locally, 2026-09-25 (Asia/Taipei)

- Two separate GPT-6 Luna Tasks were created for bounded read-only work. Their session metadata identified the requested model, and both Tasks completed.
- Two different heartbeat automations were simultaneously `ACTIVE` and targeted the same coordinating Task. Each prompt named only its own delegated Task.
- Updating the first heartbeat left the second one's saved prompt and update timestamp unchanged.
- Pausing the first heartbeat left the second `ACTIVE`; the second was then paused independently. Both saved statuses were read back as `PAUSED`.
- An initially one-minute experimental cadence was changed to 15 minutes after user feedback. The executing Tasks were told to finish without waiting for the schedule.
- The coordinator-only skill was validated with Codex skill-creator `quick_validate.py`.

## Not established by that experiment

- The heartbeats did **not** complete a timed wake-and-react cycle. Autonomous status-based prompt changes and self-pausing after a scheduled wake remain unverified.
- The skill is a set of instructions, not a native event hook. Model selection and tool availability can affect whether it is applied.

The repository check (`python3 scripts/check.py`) verifies the published package's basic structure and image constraints. It does not change these runtime limits.
