# LangGraph

Place `phion_before_model` before provider/tool selection. Set
`phion_task_capability` to one of the 15 supported public capability labels;
optionally provide `phion_constraints` or `required_provider`.

The node returns advisory pre-resolution state only. It does not copy the raw
prompt, authorize payment, or execute the selected provider.
