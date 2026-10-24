# T31 destructive content operations through the default SDK

Use `client.query.command_search(...)` and `client.query.command_usage(...)` to obtain the
minimal call, then call the default generated SDK method. The active set is:

- `client.asset.delete`, `client.asset.fixup_redirectors`, `client.asset.move`, `client.asset.object_clone`
- `client.modeling.voxel_bounds_remove`
- `client.skeletal_mesh.remove_morph_target`, `client.skeletal_mesh.remove_skin_weight_profile`
- `client.world.level_content_delete_scope`, `client.world.pcg_cleanup`

`ueagentinterfacecmd ... exec <command-name>` uses the same exact binding. There is no
task-specific generated SDK authority.

Persistent mesh, material-slot, Data Layer, and streaming-level edits use the
current HJSON workspace. `modeling.actor.mesh.replace`,
`modeling.asset.material_slot.remove`, `world.data_layer.delete`,
`world.level_streaming.move_actors`, and `world.level_streaming.remove` are dormant
compatibility bindings, not current discovery or authoring entries.

`client.asset.object_clone(source_ref, target_ref)` accepts package paths
(`/Game/Folder/Asset`) and matching object paths (`/Game/Folder/Asset.Asset`).
The source may be under `/Game` or `/Engine`; the new target must be under `/Game`.
Successful execution returns `ok=true` and `payload.status="committed"`; the
impact scope lists affected packages, not asset object-path records. When needed,
read the asset with `client.asset.registry_record(target)` to obtain its object path.
`target` accepts the complete readable asset name returned by `query.content.search`;
use the resulting `assets[].object_path` for operations whose arguments require paths.
A reference input failure identifies
`/source_ref` or `/target_ref` in `error.diagnostic.json_pointer` and supplies a
readable correction; an invalid target says nothing about source availability.

Read-only source packages may contain unsaved edits: clone reads the current
resident source without saving it. A package that is also in the write scope remains a write
target. Unsaved write targets return `error.diagnostic` with the precise cause,
package, and recovery action; the caller does not need to guess from the outer
`destructive_plan_rejected` code. Clone does not require `confirm=true`.

Use `client.asset.delete(targets, recursive=False)` for asset deletion.
`targets` is a non-empty array of `/Game` asset object paths, package names,
Content Browser package folders, or a mixture; a single target is still a
one-item array. Exact assets resolve before folders. `recursive=False` selects
only direct assets in a folder; `recursive=True` includes nested descendants.
Planning returns the normalized, sorted, overlap-free actual target set. Commit
reports each target as `deleted`, `blocked`, or `remaining` with its own reason
and independent readback. Partial deletion is returned as a failed command with
the complete projection. The SDK performs no filesystem deletion or selection
expansion.

Dependencies between selected targets are internal to the batch, including when
only some targets are already loaded. The plugin completes the native pending
set with selected referencers of loaded assets; it does not select or delete
outside referencers, and unrelated unloaded targets retain the durable-only path.
Execution preserves each target's `error_detail`, `terminal_state`, and `readback`.
Native reference refusal identifies the remaining disk package and memory object
referencers after UE's pending-set containment filtering. Same-package objects,
Blueprint generated classes, and references from another pending target are not
reported as external blockers. A rolled-back peer points to batch `failure_reason`
rather than claiming that every selected asset had its own reference blocker.
`rolled_back` confirms restored persisted content and required native asset state;
restoring files alone is insufficient. The original operation error is retained
separately from any unconfirmed recovery reported in `failure_reason`.

Deleting an ordinary registered SoundSubmix includes native audio-device
unregistration. Required/default device submixes and active source voices are
refused, and normal asset-reference checks still apply. Failure recovery rebinds
the restored asset's registration/root state by path; it does not restore transient
recording buffers, DSP history, or external buffer listeners. An unverified
recovery remains `state_unknown`. Check the complete terminal result rather than
assuming that an absent asset file proves deletion.

A clean open asset editor is closed through Unreal's native deletion path.
Readback distinguishes `package_empty` from `package_absent`, and
`object_retired` from `object_absent`: native references can delay memory cleanup
after asset ownership has ended. Success still requires no file/registry entry,
an absent or empty package, and an absent object or one no longer classified as
an asset and without public/standalone flags.

For `client.world.level_content_delete_scope`, `folder_path` is required and
`managed_id` is optional. Omitting `managed_id` requests the broad folder and
descendant scope. Supplying it requests the exact intersection of that folder
and one canonical UAI-managed actor identity; callers must pass the same values
for plan and authorized commit. Duplicate, absent, or folder-mismatched managed
identities are rejected by the plugin before mutation.

Every destructive request performs complete preflight first. Where the
contract requires two phases, the service retains authorization state
internally across the managed operation; the SDK never accepts, invents,
stores, or echoes an authorization identity. Success requires the native mutation, persistence,
independent absence/state readback, and cleanup terminal result. Invalid,
stale, or mismatched authorization fails before write.
