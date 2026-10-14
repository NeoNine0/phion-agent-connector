# OpenAI Agents SDK

Wrap `find_service_for_task` with the SDK's `function_tool` and add it to the
agent's tools. Its task-oriented description covers the 15 currently supported
PHION capability families, so the model can select it from ordinary task
language without knowing the name `phion_resolve`.

The function sends only the selected capability label and allowed constraints.
It never forwards conversation text, pays, or executes a provider. An explicit
provider mandate bypasses resolution.
