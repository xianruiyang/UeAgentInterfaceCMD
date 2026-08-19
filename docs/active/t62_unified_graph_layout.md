# Unified graph layout through the default SDK

Use `client.query.command_search(...)` and
`client.query.command_detail(...)` to obtain the current contract, then invoke
the only public persistent layout entry:

```python
result = client.graph.layout_apply(
    targets=[
        {
            "graph_identity": "/Game/UI/BP_Menu.BP_Menu:EventGraph",
            "expected_revision": "graph-layout:0123abcd",
        }
    ],
    strategy="hierarchical_left_to_right",
    parameters={"horizontal_spacing": 320, "vertical_spacing": 160},
    authorization_id="auth:layout:menu",
)
```

`targets` may contain one graph or multiple exact graphs from different
supported domains. The service routes by real graph type, preflights the whole
set, saves all affected packages, and returns an `impact_plan` plus
`independent_readback`. Callers do not select a provider and there are no
Blueprint, Material, Niagara, PCG, AI, Audio, Animation Blueprint, or Control
Rig layout aliases. The exact `uai-cli` invocation uses the same ID, hash, and
JSON parameter object.
