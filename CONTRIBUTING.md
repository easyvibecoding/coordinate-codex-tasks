# Contributing

Issues and focused pull requests are welcome. Keep the skill small: add instructions only when they improve a real decision or preserve an important boundary.

## Before opening a pull request

1. Explain the user scenario and the failure or ambiguity it addresses.
2. Preserve explicit authorization for separate Task creation and external actions. The worker Task should not need to run this coordination skill.
3. Keep each monitor scoped to one delegated Task, use a proportionate cadence, and avoid unchanged status chatter.
4. Run `python3 scripts/check.py`. If you have the Codex skill-creator tooling locally, also run its `quick_validate.py` against the repository root.
5. Describe what was actually tested. Do not present a packaging check or a manually updated automation as proof of autonomous scheduled wake behavior.

Please avoid including task transcripts, tokens, private paths, credentials, or production data in issues and pull requests.
