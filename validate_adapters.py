"""Dependency-free safety canary for PHION's public thin adapters."""
from pathlib import Path
import importlib.util
import sys

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "integrations/upra"))

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

upra = load("phion_upra", ROOT / "integrations/upra/phion_upra.py")
task_entry = load("phion_task_entry", ROOT / "integrations/upra/phion_task_entry.py")
assert upra.resolve(upra.Requirement(capability="local", external=False))["reason"] == "LOCAL_NO_OP_PATH"
assert upra.resolve(upra.Requirement(capability="search", explicit_provider="mandated"))["reason"] == "EXPLICIT_PROVIDER_MANDATE_BYPASS"
assert len(task_entry.SUPPORTED_TASKS) == 15
assert task_entry.resolve_task("unsupported")["reason"] == "UNSUPPORTED_OR_AMBIGUOUS_TASK"
assert task_entry.resolve_task("unsupported")["paymentAuthorized"] is False
seen = {}
original_resolve = task_entry.resolve
task_entry.resolve = lambda requirement: seen.update({"requirement": requirement}) or {"state":"ABSTAIN"}
task_entry.resolve_task("search")
task_entry.resolve = original_resolve
assert seen["requirement"].capability == "search"
assert not hasattr(seen["requirement"], "prompt")

for name, relative in {
    "langgraph": "integrations/langgraph/phion_before_model.py",
    "openai_agents": "integrations/openai-agents/phion_filter.py",
    "google_adk": "integrations/google-adk/phion_callback.py",
    "strands": "integrations/strands/phion_hook.py",
}.items():
    adapter = load(name, ROOT / relative)
    if hasattr(adapter, "find_service_for_task"):
        assert "search" in adapter.find_service_for_task.__doc__.lower()

print("adapter_canary=PASS payments=0 executions=0 raw_prompts=0")
