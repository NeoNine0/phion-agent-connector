"""LangGraph before-model middleware helper with no payment authority."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "upra"))
from phion_upra import Requirement, resolve
from phion_task_entry import TASK_DISCOVERY_DESCRIPTION, SUPPORTED_TASKS, resolve_task

def phion_before_model(state, runtime=None):
    bounded_task = state.get("phion_task_capability")
    if bounded_task:
        return {"phion_pre_resolution": resolve_task(
            bounded_task,
            constraints=state.get("phion_constraints"),
            explicit_provider=state.get("required_provider"),
        )}
    requirement = state.get("phion_requirement")
    if not requirement:
        return None
    value = requirement if isinstance(requirement, Requirement) else Requirement(**requirement)
    return {"phion_pre_resolution": resolve(value)}

