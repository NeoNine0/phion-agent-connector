"""Factory used immediately before an OpenAI Agents SDK model call.

The caller owns requirement extraction and supplies a bounded capability.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "upra"))
from phion_upra import Requirement, resolve
from phion_task_entry import TASK_DISCOVERY_DESCRIPTION, SUPPORTED_TASKS, resolve_task

def find_service_for_task(capability: str, constraints=None, explicit_provider=None):
    """Task-facing function suitable for wrapping with the SDK's function_tool."""
    return resolve_task(capability, constraints=constraints, explicit_provider=explicit_provider)

find_service_for_task.__doc__ = TASK_DISCOVERY_DESCRIPTION

def resolve_requirement(requirement):
    if not requirement:
        return {"state": "ABSTAIN", "reason": "NO_EXTERNAL_REQUIREMENT"}
    value = requirement if isinstance(requirement, Requirement) else Requirement(**requirement)
    return resolve(value)

def make_call_model_input_filter(requirement_factory, attach_result):
    """Return a call_model_input_filter without assuming an SDK state schema."""
    def filter_model_input(data):
        result = resolve_requirement(requirement_factory(data))
        return attach_result(data, result)
    return filter_model_input

