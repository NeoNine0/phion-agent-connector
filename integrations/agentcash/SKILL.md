---
name: phion-pre-resolution
description: Resolve an external capability through PHION before provider search, without granting payment authority.
license: Apache-2.0
compatibility: agentcash, claude, openai
---

# PHION Pre-Resolution

When an external capability is needed and no provider was mandated, send only a generic capability label and bounded constraints to `POST https://phion.systems/v1/resolve` with `executionMode: ADVISORY`.

Accept only `SINGLE_ELIGIBLE_CANDIDATE`, `ABSTAIN`, or `ADVISORY_COMPARISON_AVAILABLE`. Resolution never authorizes payment. AgentCash remains responsible for its wallet, spending policy and paid call. Skip PHION for local work or explicit provider mandates. Abstain on timeout or malformed output.

Never send credentials, private keys, wallet signatures, full prompts or unnecessary personal data.
