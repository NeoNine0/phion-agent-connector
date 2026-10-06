"""Google ADK before-model callback helper; advisory and fail-open."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "upra"))
from phion_upra import Requirement, resolve

def make_before_model_callback(requirement_factory, store_result):
    def before_model_callback(callback_context, llm_request):
        supplied = requirement_factory(callback_context, llm_request)
        if supplied:
            value = supplied if isinstance(supplied, Requirement) else Requirement(**supplied)
            store_result(callback_context, resolve(value))
        return None
    return before_model_callback

