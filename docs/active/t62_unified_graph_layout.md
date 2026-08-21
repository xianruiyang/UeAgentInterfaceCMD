# Unified graph layout through the default SDK

Use `client.query.command_search(...)` and
`client.query.command_detail(...)` to obtain the current contract, then invoke
the only public persistent layout entry:

```python
result = client.graph.layout_apply(
    targets=[
        {
            "graph_identity": "/Game/UI/BP_Menu.BP_Menu:EventGraph",
            "expected_revision": "content-graph:0123abcd",
        }
    ],
    strategy="hierarchical_left_to_right",
    parameters={"horizontal_spacing": 320, "vertical_spacing": 160},
    authorization_id="auth:layout:menu",
)
```

`targets` may contain one graph or multiple exact graphs only from the same
owning Blueprint asset and package. Read the owner with `content_graph.*` and
use its public `revision` as every target's `expected_revision`. The service
routes by the real owner type, measures geometry offscreen, preflights the whole
set, compiles and saves the package, reloads it, and returns an `impact_plan`, a
`persistence_receipt`, and persisted positions in `independent_readback`.

Blueprint, Widget Blueprint, and Animation Blueprint are the current verified
provider families. Cross-package batches and Material, Niagara, PCG, AI, Audio,
and Control Rig layout are rejected until those verticals contribute real
mechanics. Callers do not select a provider. The exact `uai-cli` invocation uses
the same command ID and JSON parameter object.
