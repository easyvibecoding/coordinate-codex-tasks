# Coordinate Codex Tasks

![A coordinator with three separately monitored tasks](assets/social-preview.jpg)

**A Codex skill for delegating work to separate Codex Tasks while the original Task stays responsible for coordination and verification.** It creates one dedicated, state-aware heartbeat per delegated Task, keeps each monitor scoped to its own Task, and pauses it when the work is verified complete or needs a user decision.

[繁體中文](README.zh-TW.md) · [Skill instructions](SKILL.md) · [Verification record](docs/verification.md)

This is an independent community skill. It is not an official OpenAI product.

## Why use it?

A separate Codex Task can keep working after its coordinator yields. The coordinator needs a durable way to check progress without repeatedly interrupting the worker, losing the assignment boundary, or treating `idle` as proof of completion. This skill describes that workflow using Codex Task and automation tools.

## Behavior

- Creates a separate Task **only when the user explicitly requests one**.
- Distinguishes an independent, user-owned Task from a Task delegated to complete part of the coordinator's assignment.
- For delegated work, maintains a one-to-one mapping between worker Task and heartbeat. Multiple workers can have distinct heartbeats attached to the same coordinating Task.
- Starts with a proportionate cadence, around 15 minutes for ordinary long-running work. Unchanged checks stay quiet; active coordination uses `wait_threads` instead of faster schedules.
- Reads the worker's current state and relevant artifacts before updating the monitor prompt, giving a scoped correction, or pausing the monitor. A finished turn is not necessarily a finished assignment.
- Leaves the worker focused on its work. The **coordinator** uses this skill; workers do not need to load it to manage their monitors.

The skill is guidance for the model, not an event hook or a guaranteed background daemon. Scheduled runs require the relevant Codex app tools and an available host. See [verification limits](docs/verification.md).

## Requirements

- Codex with Skills enabled.
- Access to the Codex app Task tools (`create_thread`, `wait_threads`, `read_thread`, `send_message_to_thread`) and `automation_update` for scheduled monitoring.
- The user's authorization to create a separate Task. Ordinary internal subtasks should use the available subagent mechanism.

## Install

```sh
git clone https://github.com/easyvibecoding/coordinate-codex-tasks.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills/coordinate-codex-tasks"
cp coordinate-codex-tasks/SKILL.md "${CODEX_HOME:-$HOME/.codex}/skills/coordinate-codex-tasks/SKILL.md"
```

Then start a new Codex Task so it can discover the skill. You can invoke it explicitly:

```text
Use $coordinate-codex-tasks. Create a separate Codex Task to implement the parser change. Keep this Task responsible for review and integration.
```

For an independent Task that you will follow directly, say so. The skill will dispatch it without creating a coordinator monitor.

## State policy

| Worker evidence | Coordinator action |
| --- | --- |
| Active, no verified change | Keep its heartbeat active; do not rewrite the prompt or send a status message. |
| New stage or recoverable blocker | Update only its heartbeat checkpoint; send one specific correction if needed. |
| Idle or turn completed, assignment unfinished | Inspect the result and artifacts; continue the same Task when authorized. |
| Outcome verified, terminal blocker, or user decision required | Pause only its heartbeat, read back the saved status, and report once. |

The actual [SKILL.md](SKILL.md) is the operational source. The table summarizes its decisions.

## Development

Run the repository's dependency-free package check:

```sh
python3 scripts/check.py
```

The check validates packaging and the social preview asset; it does not prove model behavior. See [CONTRIBUTING.md](CONTRIBUTING.md) for change guidance.

## License

[MIT](LICENSE). The social preview artwork was generated with Codex image generation and is included in this repository.
