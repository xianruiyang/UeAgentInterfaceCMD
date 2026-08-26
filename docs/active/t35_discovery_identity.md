# T35 discovery and direct identity reuse

Use the generated public SDK bindings for current command, existing-content,
and domain-candidate discovery. Do not call HTTP directly and do not translate
returned identities in client code.

```python
with uai.connect("connection.toml") as client:
    found = client.query.command_search("query.content.search", limit=8)
    exact = next(
        item
        for item in found.payload["candidates"]
        if item["command_id"] == "query.content.search"
    )
    client.query.command_detail(exact["command_id"], exact["contract_hash"])

    assets = client.query.content_search(
        query="/Game/UAI/M_Test.M_Test",
        match_mode="exact",
        content_kinds=["asset"],
        required_operations=["query"],
        limit_per_provider=4,
    )
    asset_identity = assets.payload["items"][0]["identity"]
    client.asset.summary(asset_identity)
```

The current unified providers cover Asset Registry assets and current Editor
World Actors and Components. Copy `next_cursor` unchanged while keeping the same
query and filters. A cursor is revision-fenced and is not a resumable identity
after provider state changes.

Creation candidates are deliberately domain-owned. Use the matching generated
binding—`ai.behavior_candidates`, `animation_rig_graph.candidates`,
`audio.graph_candidates`, `blueprint.component_candidates`,
`blueprint.node_candidates`, `material.expression_candidates`,
`niagara.module_candidates`, or `pcg.node_candidates`—then read that exact
command detail. Domains already on the contextual-create contract copy only a
compact candidate `name` or `id`; graph, pin, parent, level, stage, placement,
and instance identity stay in the owning HJSON context. A legacy field remains
valid only while the current command detail declares it. `query.content.search`
does not aggregate or reinterpret those candidate mechanics.

The public product receipt is stored under
`runtimeLogs/uai-development/TROOT-UAI-35-DISCOVERY-IDENTITY-VERTICAL/20260820-r3/public_sdk_product/receipt.json`.
It proves one current Material candidate-to-HJSON vertical and representative
Asset/Actor/Component identity reuse, not every candidate domain or every query
command.
