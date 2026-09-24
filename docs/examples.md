# Prompt examples

[繁體中文](examples.zh-TW.md) · [Back to README](../README.md)

Paste a prompt into the **current coordinating Task**. Replace bracketed text with your real work and acceptance evidence. A separate Codex Task is created only when you explicitly ask for one. `$coordinate-codex-tasks` invokes the skill explicitly; scheduled wakes and tools still depend on the Codex environment.

## 1. Delegate one new Task and keep review here

```text
Use $coordinate-codex-tasks. Create a separate Codex Task to complete [specific objective], limited to [files or module]. Acceptance evidence: [checkable result or command]. Keep this Task responsible for integration and review. Confirm the new Task has started, create one dedicated monitor for it, update the checkpoint only when evidence changes, and pause its monitor after the outcome is verified.
```

## 2. Delegate two Tasks with separate monitors

```text
Use $coordinate-codex-tasks. Create two separate Codex Tasks. Task A owns [work, scope, acceptance evidence]; Task B owns [different work, scope, acceptance evidence]. They should not edit the same files. Keep integration and review in this Task. Give each delegated Task its own monitor, starting around a 15-minute interval for ordinary work. Stay quiet when nothing meaningful changes. Do not combine both Tasks into one monitor or ask the workers to manage scheduling.
```

## 3. Continue an existing Task

```text
Use $coordinate-codex-tasks. Continue this existing Codex Task: [paste its codex://threads/... link]. Its assignment is [objective]; its verified checkpoint is [actual progress]; it still needs [next step and acceptance evidence]. Keep review in this Task. Read its current state and artifacts first. If it already has a dedicated monitor, update that monitor instead of creating a duplicate Task or monitor.
```

## 4. Hand an independent Task to the user

```text
Use $coordinate-codex-tasks. Create a separate, independent Codex Task for [objective and acceptance evidence]. I will follow up in that Task myself. Confirm it started and give me its link. Do not create a coordinator monitor for it.
```

## 5. Delegate without scheduled monitoring

```text
Use $coordinate-codex-tasks. Create a separate Codex Task for [objective and acceptance evidence], while this Task remains responsible for final review. Do not create a scheduled monitor this time. During the current turn, use the available wait tool to follow progress and inspect the worker's actual result when needed.
```

These prompts establish ownership and checkpoints; they do not reserve continuous model attention. Scheduled wake-and-react behavior is bounded by the evidence in the [verification record](verification.md).
