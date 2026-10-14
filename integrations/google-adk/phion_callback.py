"""Google ADK before-model callback helper; advisory and fail-open."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "upra"))
from phion_upra import Requirement, resolve
from phion_task_entry import TASK_DISCOVERY_DESCRIPTION, SUPPORTED_TASKS, resolve_task

def find_service_for_task(capability: str, constraints=None, explicit_provider=None):
    """Task-facing function that can be supplied in a Google ADK tools list."""
    return resolve_task(capability, constraints=constraints, explicit_provider=explicit_provider)

find_service_for_task.__doc__ = TASK_DISCOVERY_DESCRIPTION

def make_before_model_callback(requirement_factory, store_result):
    def before_model_callback(callback_context, llm_request):
        supplied = requirement_factory(callback_context, llm_request)
        if supplied:
            value = supplied if isinstance(supplied, Requirement) else Requirement(**supplied)
            store_result(callback_context, resolve(value))
        return None
    return before_model_callback

