"""Task-facing PHION entry shared by framework adapters.

The host agent selects one bounded capability from a public enum. Conversation
text is never sent or stored, and resolution never authorizes payment or
execution.
"""
from __future__ import annotations

from typing import Any, Mapping

from phion_upra import Requirement, resolve

TASK_DISCOVERY_MANIFEST = "https://phion.systems/.well-known/phion-task-discovery.json"
SUPPORTED_TASKS = (
    "market_research",
    "search",
    "inference",
    "data_enrichment",
    "web_evidence",
    "compliance",
    "payment_safety",
    "security_preflight",
    "provider_comparison",
    "capability_verification",
    "agent_trust",
    "transaction_assurance",
    "data_transformation",
    "onchain_data",
    "customer_support",
)

TASK_DISCOVERY_DESCRIPTION = """Use before choosing an external provider when
the agent needs current search, inference, market research, company/person data
enrichment, source-backed evidence, compliance screening, payment safety,
integration security, provider comparison, capability verification, agent
trust, transaction assurance, schema normalization, on-chain information, or
customer-support processing. Select the closest supported task. This advisory
step compares eligible offers through PHION; it never pays or executes."""


def resolve_task(
    capability: str,
    *,
    constraints: Mapping[str, Any] | None = None,
    explicit_provider: str | None = None,
    external: bool = True,
    sensitive: bool = False,
):
    """Resolve a bounded task without transmitting the originating prompt."""
    if capability not in SUPPORTED_TASKS:
        return {
            "state": "ABSTAIN",
            "reason": "UNSUPPORTED_OR_AMBIGUOUS_TASK",
            "paymentAuthorized": False,
            "executionAuthorized": False,
        }
    return resolve(Requirement(
        capability=capability,
        constraints=constraints or {},
        explicit_provider=explicit_provider,
        external=external,
        sensitive=sensitive,
    ))
