# Universal Pre-Resolution Adapter

UPRA calls the existing `phion_resolve` endpoint in advisory mode. It is optional, removable and provider-neutral. It has local no-op and explicit-provider bypass paths, a 1.5 second latency budget and fail-safe abstention. It sends a generic capability label rather than conversation text.

The only resolver recommendation states accepted are `SINGLE_ELIGIBLE_CANDIDATE`, `ABSTAIN` and `ADVISORY_COMPARISON_AVAILABLE`. Installation does not authorize payment or execution.

`phion_task_entry.py` adds a task-facing entry for framework tool discovery. The
host chooses one of 15 public task capabilities and sends only that bounded
label—not conversation text—to the same resolver. Unsupported or ambiguous
tasks abstain locally. Canonical task metadata is published at
`https://phion.systems/.well-known/phion-task-discovery.json`.
