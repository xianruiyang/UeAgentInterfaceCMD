# Non-HJSON Query SDK and CLI

`asset.registry_record` keeps its default identity summary compact. Request
`include_tags=true` for native Registry tag strings or `include_chunk_ids=true`
for its integer chunk array (possibly empty); omitted/false options omit them.
Explicitly returned business arrays/maps retain empty results, including nested
and record-array fields. Missing optional fields remain absent.
`asset.collection` without `field_ids` returns the native collection-field names
and counts under `fields`, so a subsequent value query can select actual fields.
`world.mesh_vertex_position` and `world.mesh_closest_vertex` take the actual
StaticMesh or DynamicMesh component identity. Their `vertex_index` is a
zero-based position in ascending live vertex-ID order for the current topology,
not an Actor, asset, or persistent vertex identity. StaticMesh uses source LOD 0;
both paths transform local vertices through the component into world space.

`client.asset.sample(mesh, input={"sample_kind":"section", "index":0})`
reads one StaticMesh LOD 0 render section; omitted index selects 0. Its sample
includes section/slot counts, triangle count, actual material index/path,
`material_index_valid`, and current/original section-map indices. An invalid
material index is observable with an empty path; an invalid section index is an
error. This complements asset-local `bounds` and source-LOD0 `vertex` samples
without opening an editor or changing material slots.

Import only `uai` and use `uai.connect_project()` for the local project. The final
manifest generates the normal domain namespaces for the current Query routes:

```python
import uai

with uai.connect_project() as client:
    summary = client.project.summary(
        projection={"include_provenance": True},
    )
    graphs = client.content_graph.structure(
        "/Game/Player/BP_Player.BP_Player",
        input={"include_hierarchy": True},
        projection={"profile_id": "compact"},
    )
    nodes = client.content_graph.items(
        "/Game/Player/BP_Player.BP_Player",
        input={
            "containers": ["EventGraph"],
            "items": ["CharacterMovement"],
            "fields": ["pin_interface"],
        },
        projection={"profile_id": "compact"},
    )
    origin = client.reference.origin_resolve(
        input={"target": {
            "source": "ue_object",
            "asset_path": "/Game/UAI/Reference/BP_Reference.BP_Reference",
        }},
    )
    relations = client.asset.relations(
        "/Game/UAI/Reference/BP_Reference.BP_Reference",
        input={
            "direction": "both",
            "relation_kinds": ["hard", "soft"],
        },
    )
    heights = client.landscape.height_read(
        "uai://landscape/example",
        input={
            "region": {
                "frame_id": "ue.landscape.local_sample_grid",
                "min_inclusive": [0, 0],
                "max_inclusive": [3, 3],
            },
            "space_contract": {
                "frame_id": "ue.landscape.local_sample_grid",
                "unit": "sample",
                "basis_evidence": "exact managed target and observed extent",
            },
        },
    )
```

For a capsule path, choose whether the next action needs the first obstacle
before calling. Omit `include_first_hit` (or pass false) for the original
`{"blocked_segments": N}` summary. Request it in the same call when diagnosing:

```python
path_input = {
    "points": [
        {"frame_id": "ue.world", "unit": "centimeter", "components": [0, 0, 100]},
        {"frame_id": "ue.world", "unit": "centimeter", "components": [200, 0, 100]},
    ],
    "radius_cm": 34,
    "half_height_cm": 88,
    "step_cm": 50,
    "trace_channel": "pawn",
}
# Replace this example geometry with the intended path in the current world.
locate_obstruction = True
if locate_obstruction:
    path_input["include_first_hit"] = True
with uai.connect_project() as client:
    result = client.world.capsule_path(input=path_input)
    result.raise_for_error()
    print(result.payload["blocked_segments"])
    if locate_obstruction:
        first = result.payload["first_blocking_hit"]  # Explicit None for no blocker.
        if first is not None:
            print(first["segment_index"], first["target_ref"], first["start_penetrating"])
            print(first["shape_location"], first["impact_point"])
```

`segment_index` is zero-based in the original points array. Positions are world
centimeters; `shape_location` is the capsule center, while `impact_point` is the
native hit position. Initial penetration is explicitly marked and does not give
a precise contact surface. `target_ref` may be null when the native hit has no
Component; otherwise it is a native Component reference, not a HJSON selector.
The count still covers all input segments even though only the first blocker is
returned. A blocked path is a successful query result.

`trace_complex` defaults to false. Set it explicitly only when that collision
representation answers the current question; asset collision settings still
apply. A complex-only clear result cannot prove Pawn movement clearance.
Consume the first hit directly instead of mechanically appending a sweep for
the same blocker. Use `capsule_sweep` when all hits or its direct segment query
are needed, and `overlap` for occupancy. These static probes do not verify
runtime traversal. Full behavior is owned by the Plugin's
`docs/active/t06_non_hjson_query_migration.md`.

Settings discovery uses `client.project.settings(input={"editor_project_capability":"project_settings.index"})`; optional `parameters.container` narrows the index.
Use the returned section identity for `project_settings.page` with `parameters.section_id`. The public page retains `properties.property_path`, `kind`, authoring-coded `value` and `availability`; these queries do not write files. Canonical `input={"section_id":...,"field_ids":[...]}` resolves that same page and reads selected values under `fields`; without `field_ids` it returns a count. `include_defaults=True` adds selected UE text defaults, with `null` when an independent default is unavailable. For editing, use the index's `settings_object_path` with the ordinary HJSON workspace.

The generic forms use the same generated catalog:

```python
result = client.execute(
    "project.summary",
    {"projection": {"profile_id": "compact"}},
)
```

The CLI forwards the same request through the same Client, Protocol, and
Transport:

```text
ueagentinterfacecmd exec project.summary --params-json '{"projection":{"profile_id":"compact"}}'
```

`command_search` returns every positive match, and `command_usage` accepts any nonempty command-name list without a batch ceiling.

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery). Search matches
only positive tokens from command names, registered keywords and registered
synonyms; execute the selected command name unchanged.

Asset and ContentGraph queries accept the readable name returned by
`client.query.content_search(...)` as `target`; HJSON `export_workspace` accepts
that asset name as well. Resolution uses the current shared discovery service
on the server. Preserve any short semantic scope returned with the name.
Existing exact paths remain accepted. Existing-asset creation-candidate queries
also accept these names: Blueprint nodes/components, Material, Niagara, AI,
PCG, UMG, Rig, Audio, World Actors, and Timeline tracks. Create-only Animation
Blueprint discovery requires a future asset path; AssetFactory discovery has
no existing-asset target. Other World commands retain their own target contracts.
Missing required identities
return typed failures such as `query_target_required`. For each single
`content_graph` facet, a successful payload is directly `{"entries":[...]}`.
`content_graph.compound` instead returns a single `sections` object whose arrays
retain the requested business categories. It never exposes a cursor,
snapshot/revision, owner, selector, command envelope, or hash/GUID-like machine
identity. The generated methods add no UE business logic, alias mapping, retry
loop, transport fallback, or result reinterpretation. Non-content-graph Query
routes keep their own current contracts until separately migrated.
Shared record projections preserve observed empty business containers and
report malformed records or nested values with their public field/index path.
A single-record projection reports zero or multiple matching records instead
of silently returning an empty object or the first record. Removing private
fields does not erase an originally empty business object.

For graphs, keep discovery and focused content queries separate. Start with
`content_graph.structure`; after choosing a graph/container by its short readable
name, call `content_graph.items` with one `item_kinds` family and only the
required public `fields`. Across each single `content_graph` facet (`summary`,
`structure`, `items`, `relations`, `properties`, and `diagnostics`), success is a
direct `{"entries":[...]}` business result. `compound` returns section-grouped
arrays instead of mixing unlike entries. The public
selection fields are `containers`, `items`, `endpoints`, `owners`, `fields`, and
`roots`; their requiredness follows each facet's input schema. In particular,
`content_graph.properties` requires `owners`: use owner names returned by the
structure/items query, then narrow with `fields` as needed. Do not pass an empty
input object expecting an unfiltered property dump. Callers should request only
the fields needed for the current decision.
Requested properties report their current values, including inherited/class-default
values; a value equal to its default is not an absent property. `include_presence`
adds authored-presence information when requested. The legacy `include_defaults`
input remains accepted for compatibility and does not select an overrides-only
view or change which fields are captured.
Diagnostics are captured on demand, separately from ordinary authoring capture.
Niagara compile coverage follows the native VM owner: a standalone Emitter
definition, or an auxiliary script that UE cannot independently compile, reports
`not_applicable` for stored VM freshness. This does not certify compilation;
use the successful native-context compile result for that operation. Stored
messages remain available, and System/compilable-script stale or pending state
is not hidden.
They return a `kind: coverage` entry naming the observed native sources and their
availability, plus `kind: diagnostic` entries for actual messages. Severity filters
do not hide coverage. A query never initiates compilation, generation, or an asset
editor; pending, stale, or unavailable state is not evidence of a clean result.
Common graph-node messages, Blueprint status, stored material resource errors,
Niagara compile/Stack observations, and retained PCG execution logs keep their
native scopes. Machine identities in nested diagnostic details use the same
public identity filtering as every other content-graph facet.
Each coverage source carries `owner`, `context`, and `status`. `observed` means
that source was read, not that this operation compiled or executed it. Retained
PCG component logs have no current-generation proof; MaterialFunction preview
resources belong to the existing preview context. Blueprint Dirty/Unknown remain
stale/unknown. Native update completion comes from the executing operation's
stage evidence, independently of snapshot diagnostic availability.
The selected container and item names in the example come from the target's
structure/items results. Omit `fields` for the default item summary; `items` is a
selector, not a readable item field. Blueprint nodes omit variable pin interfaces
by default; request `pin_interface` only for selected nodes whose pins are needed.
Fields depend on the item's exposed state. Field projection checks the entire
selected item set before producing entries. Incompatible fields are reported by
item kind and field contract, with readable affected-item locations in
`related_sources`. A failure's `choose` contains compatible `items`/`containers`
selections derived from the same capture, when publicly addressable items exist;
keep the requested fields when refining the selection. This is a failed query,
not a partial result that silently omits incompatible items. When names are
unique, entries use short readable aliases. Repeated names receive stable numeric
suffixes; only cross-graph ambiguity requires `GraphAlias/NodeAlias`. No facet exposes GUIDs,
hashes, cursors, opaque internal IDs, or an envelope. Use `content_graph.compound` only when several facets are intentionally
required together; an impossible projection remains a typed refine failure.
The public query view consumes each domain's existing readable-name mapping before
selection and field projection. Item names, owner/root selectors and diagnostic
choices therefore use the same aliases; authoring baselines retain native semantic
names. `items`, `owners` and `roots` accept `GraphAlias/NodeAlias`, and relation
endpoints also accept `GraphAlias/NodeAlias.PinAlias`. An explicit `containers`
selection still limits qualified names to that scope.

`asset.registry_relations`, `asset.properties`, `asset.summary`, `world.actors`,
`world.actor_components`, `world.content`, and `world.property` are dormant. Use `asset.relations` for the token-compact typed
Asset Registry graph, and use `content_graph.structure`, filtered
`content_graph.items`, and filtered `content_graph.properties` for persisted
World content. Use `query.content.search` with the `actor` or `component` kind
for current Editor World name discovery, then use the returned
readable names and the corresponding generated SDK method, not a machine detail envelope.

Normal `query.command_search` results and generated named SDK methods do not
expose dormant commands. A known exact dormant ID can be passed through ordinary
`client.execute` or `ueagentinterfacecmd exec`;
dormancy preserves the original contract and server implementation; an exact
call uses the ordinary dispatch path.
