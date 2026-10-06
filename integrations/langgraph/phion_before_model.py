"""LangGraph before-model middleware helper with no payment authority."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "upra"))
from phion_upra import Requirement, resolve

def phion_before_model(state, runtime=None):
    requirement = state.get("phion_requirement")
    if not requirement:
        return None
    value = requirement if isinstance(requirement, Requirement) else Requirement(**requirement)
    return {"phion_pre_resolution": resolve(value)}

