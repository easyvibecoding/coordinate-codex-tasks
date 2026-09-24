# Prompt examples

[繁體中文](examples.zh-TW.md) · [Back to README](../README.md)

Paste a prompt into the **current coordinating Task**. Replace bracketed text with your real work and acceptance evidence. An explicit request to open another Codex Task can let the model select the installed skill from its description; you do not need to name the skill. Selection is a model decision, not a guaranteed hook on every Task creation.

## The user's original phrasing

In the conversation that led to this skill, the user wrote this without naming it:

```text
將這個Task當主代理Task 建多GPT-6 Luna Task 委派與排程器實驗驗證
```

It names a coordinating Task, multiple new Tasks, and a scheduling experiment. For ordinary work, replace the experiment with concrete assignments and acceptance evidence:

```text
Make this Task the coordinator. Create two separate GPT-6 Luna Codex Tasks for [work A] and [work B]. Keep integration and review here. Give each delegated Task its own monitor, update it when evidence changes, stay quiet when nothing changes, and pause each monitor after its assignment is verified.
```

## 1. Delegate one new Task and keep review here

```text
Create a separate Codex Task to complete [specific objective], limited to [files or module]. Acceptance evidence: [checkable result or command]. Keep this Task responsible for integration and review. Confirm the new Task has started, create one dedicated monitor for it, update the checkpoint only when evidence changes, and pause its monitor after the outcome is verified.
```

## 2. Delegate two Tasks with separate monitors

```text
Create two separate Codex Tasks. Task A owns [work, scope, acceptance evidence]; Task B owns [different work, scope, acceptance evidence]. They should not edit the same files. Keep integration and review in this Task. Give each delegated Task its own monitor, starting around a 15-minute interval for ordinary work. Stay quiet when nothing meaningful changes. Do not combine both Tasks into one monitor or ask the workers to manage scheduling.
```

## 3. Continue an existing Task

```text
Continue this existing Codex Task: [paste its codex://threads/... link]. Its assignment is [objective]; its verified checkpoint is [actual progress]; it still needs [next step and acceptance evidence]. Keep review in this Task. Read its current state and artifacts first. If it already has a dedicated monitor, update that monitor instead of creating a duplicate Task or monitor.
```

## 4. Hand an independent Task to the user

```text
Create a separate, independent Codex Task for [objective and acceptance evidence]. I will follow up in that Task myself. Confirm it started and give me its link. Do not create a coordinator monitor for it.
```

## 5. Delegate without scheduled monitoring

```text
Create a separate Codex Task for [objective and acceptance evidence], while this Task remains responsible for final review. Do not create a scheduled monitor this time. During the current turn, use the available wait tool to follow progress and inspect the worker's actual result when needed.
```

Creating a new Task does not always call for a coordinator monitor. Monitoring depends on whether the current Task retains responsibility for follow-through and on your explicit instructions. These prompts do not reserve continuous model attention; scheduled wake-and-react behavior is bounded by the evidence in the [verification record](verification.md).
