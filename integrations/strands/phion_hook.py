"""Strands HookProvider for advisory PHION pre-resolution.

The host supplies a bounded external requirement. The hook never extracts a
raw prompt, pays, executes, or overrides an explicitly mandated provider.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1] / "upra"))
from phion_upra import Requirement, resolve


class PhionPreResolutionHook:
    def __init__(self, requirement_factory):
        self.requirement_factory = requirement_factory

    def register_hooks(self, registry):
        from strands.hooks import BeforeModelCallEvent
        registry.add_callback(BeforeModelCallEvent, self.before_model_call)

    def before_model_call(self, event):
        supplied = self.requirement_factory(event)
        if not supplied:
            return
        requirement = supplied if isinstance(supplied, Requirement) else Requirement(**supplied)
        event.invocation_state["phion_pre_resolution"] = resolve(requirement)

