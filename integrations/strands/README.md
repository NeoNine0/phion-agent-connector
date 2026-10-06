# Strands

Register `PhionPreResolutionHook` in `Agent(hooks=[...])`. The callback uses the
official `BeforeModelCallEvent`, stores only an advisory result in invocation
state, and leaves model, tool, execution and payment authority with the host.
The host must provide a bounded capability; the adapter never copies a raw
prompt to PHION.

