# Universal Pre-Resolution Adapter

UPRA calls the existing `phion_resolve` endpoint in advisory mode. It is optional, removable and provider-neutral. It has local no-op and explicit-provider bypass paths, a 1.5 second latency budget and fail-safe abstention. It sends a generic capability label rather than conversation text.

The only resolver recommendation states accepted are `SINGLE_ELIGIBLE_CANDIDATE`, `ABSTAIN` and `ADVISORY_COMPARISON_AVAILABLE`. Installation does not authorize payment or execution.
