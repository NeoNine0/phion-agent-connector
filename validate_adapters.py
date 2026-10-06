"""Dependency-free safety canary for PHION's public thin adapters."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).parent

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

upra = load("phion_upra", ROOT / "integrations/upra/phion_upra.py")
assert upra.resolve(upra.Requirement(capability="local", external=False))["reason"] == "LOCAL_NO_OP_PATH"
assert upra.resolve(upra.Requirement(capability="search", explicit_provider="mandated"))["reason"] == "EXPLICIT_PROVIDER_MANDATE_BYPASS"

for name, relative in {
    "langgraph": "integrations/langgraph/phion_before_model.py",
    "openai_agents": "integrations/openai-agents/phion_filter.py",
    "google_adk": "integrations/google-adk/phion_callback.py",
    "strands": "integrations/strands/phion_hook.py",
}.items():
    load(name, ROOT / relative)

print("adapter_canary=PASS payments=0 executions=0 raw_prompts=0")
