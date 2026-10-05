"""Thin, dependency-free PHION pre-resolution client.

It sends a bounded generic task/capability to the public advisory resolver. It
never pays, executes, stores prompts, or overrides an explicit provider.
"""
from dataclasses import dataclass, field
import json, os
from typing import Any, Mapping
from urllib.request import Request, urlopen

ENDPOINT = "https://phion.systems/v1/resolve"
STATES = {"SINGLE_ELIGIBLE_CANDIDATE", "ABSTAIN", "ADVISORY_COMPARISON_AVAILABLE"}

@dataclass(frozen=True)
class Requirement:
    capability: str
    constraints: Mapping[str, Any] = field(default_factory=dict)
    explicit_provider: str | None = None
    external: bool = True
    sensitive: bool = False

def resolve(requirement: Requirement, timeout: float = 1.5) -> Mapping[str, Any]:
    if os.getenv("PHION_PRE_RESOLUTION_DISABLED", "").lower() in {"1", "true", "yes"}:
        return {"state":"ABSTAIN", "reason":"DISABLED_BY_OPERATOR"}
    if not requirement.external:
        return {"state":"ABSTAIN", "reason":"LOCAL_NO_OP_PATH"}
    if requirement.explicit_provider:
        return {"state":"ABSTAIN", "reason":"EXPLICIT_PROVIDER_MANDATE_BYPASS", "provider":requirement.explicit_provider}
    allowed = {"maxPrice","currency","deadlineMs","freshnessSeconds","minimumQuality","requireVerification","allowedNetworks","allowedAssets","allowedProviders","excludedProviders","jurisdiction","privacy"}
    constraints = {k:v for k,v in requirement.constraints.items() if k in allowed}
    payload = {"task":f"Resolve external {requirement.capability} capability","capability":requirement.capability[:120],"constraints":constraints,"executionMode":"ADVISORY"}
    try:
        req = Request(ENDPOINT, data=json.dumps(payload).encode(), headers={"content-type":"application/json","x-phion-discovery-source":"public-upra"}, method="POST")
        with urlopen(req, timeout=timeout) as response:
            value = json.load(response)
        state = value.get("recommendation", {}).get("state")
        if state not in STATES: raise ValueError("unexpected resolver state")
        return {"state":state,"resolutionId":value.get("resolutionId"),"recommendation":value.get("recommendation"),"paymentAuthorized":False,"executionAuthorized":False}
    except Exception:
        return {"state":"ABSTAIN","reason":"REQUIRE_MORE_INFORMATION_LOCAL_POLICY" if requirement.sensitive else "PHION_UNAVAILABLE_OR_MALFORMED"}
