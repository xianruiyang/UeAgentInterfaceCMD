# Selected candidate property defaults

The existing Material expression, PCG node, UMG widget and audio graph candidate
queries accept optional `describe={"name": "<returned name>", "fields": ["<property>"]}`.
Use `select` inside `describe` only when the creation selector requires it.
Omitting `describe` retains the compact name-list search with shared query `scope`.
`scope` identifies the target/context once, and is not copied into candidate or properties.
This is an optional
way to discover initial properties; it does not add a required creation step.

Niagara module, Control Rig, AI behavior and animation state-machine queries also
accept `describe={"name": "<returned name>"}` in the same target and native context.
Material, Niagara, PCG, UMG, Control Rig, AI behavior and animation state-machine descriptions expose
`creation: {supported: true|false, reason: "..."}` from the native candidate owner.
A searchable name is not a promise of current HJSON creation support. Unsupported
actions remain describable without creating an instance or failing as a write.
Niagara, Control Rig, AI behavior and animation state-machine descriptions report
creation support only; requested editable fields are listed as `unavailable_fields`.
Read those fields and dynamic interfaces from the created item's export. Niagara
and Control Rig use the complete returned name, without a separate `select` map.
AI behavior keeps any attachment or inner-graph context outside `describe`.
Animation state-machine description uses the same future create-only target,
`surface` and `class_settings` as its ordinary query.

`description.properties` is the existing writable descriptor array:
`[{property_path: "DefaultValue", kind: "float", value: {literal: 0.0}}, ...]`.
Copy the needed descriptors into the new item's inline `properties`, editing
their `value` directly. Type metadata comes from native reflection and does not
require a separate type catalog or conversion from category rows. Only fields
allowed by the domain's existing authoring property policy are included;
`unavailable_fields` identifies requested fields outside that policy. Omitting
`fields` requests all exposed fields for that one candidate, not every search hit.

| Candidate | Default source | Boundary |
| --- | --- | --- |
| Material expression | Native expression class defaults | Function-specific and dynamic pins require the created graph context. |
| Native UMG widget | Native widget class defaults | Parent slot and structural widget flags have their own authoring owners. |
| SoundCue node | Native sound-node class defaults | Child-node connections remain graph structure. |
| PCG native element | Transient settings initialized with the selected native preconfiguration | The target graph is unchanged; pins are not synthesized. |
| Niagara stack action | Native action's current creation support | No module or hypothetical input defaults are created by description. |
| Control Rig native action | Native action's current creation support and `action_kind` | Support follows the shared node-family creation/persistence contract. Pins require the created graph context. |
| AI behavior native action | Native action's current creation support in the selected blank/attachment/inner-graph context | Description creates no behavior item or editable-field prototype. |
| Animation state-machine action | Native action's current creation support in the same-factory transient context | The future target remains create-only; description creates no persisted graph node. |
| PCG action outside the current creation contract | `basis: native_menu_action` and `creation.supported: false` | Description does not imply that creating an instance will make it writable. |
| MetaSound | `basis: requires_created_instance` | No class defaults are substituted for a dynamic action. |

For an existing item, edit its current exported properties. Candidate defaults
are creation guidance and must not overwrite existing values. Other dynamic
candidate interfaces continue to use their existing instance readback contracts.

Inline seeds also accept their existing `uai.uobject_properties.v2` document
wrapper. Explicit malformed payloads are diagnosed before apply, rather than
silently ignored. Exported `properties.hjson` continues to use its ordinary
category/name/type/value layout; it is not an inline creation payload.
