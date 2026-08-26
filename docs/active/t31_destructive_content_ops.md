# T31 destructive content operations through the default SDK

Use `client.query.command_search(...)` and `client.query.command_detail(...)` to obtain the
current contract and hash, then call the default named method. The active set is:

- `client.asset.delete`, `client.asset.fixup_redirectors`, `client.asset.move`, `client.asset.object_clone`
- `client.modeling.actor_mesh_replace`, `client.modeling.asset_material_slot_remove`, `client.modeling.voxel_bounds_remove`
- `client.skeletal_mesh.remove_morph_target`, `client.skeletal_mesh.remove_skin_weight_profile`
- `client.world.data_layer_delete`, `client.world.level_content_delete_scope`
- `client.world.level_streaming_move_actors`, `client.world.level_streaming_remove`, `client.world.pcg_cleanup`

`uai-cli ... exec <command-id>` uses the same exact binding. There is no
task-specific generated SDK authority.

For `client.world.level_content_delete_scope`, `folder_path` is required and
`managed_id` is optional. Omitting `managed_id` requests the broad folder and
descendant scope. Supplying it requests the exact intersection of that folder
and one canonical UAI-managed actor identity; callers must pass the same values
for plan and authorized commit. Duplicate, absent, or folder-mismatched managed
identities are rejected by the plugin before mutation.

Every destructive request performs complete preflight first. Where the
contract requires two phases, the first call returns the exact authorization
identity and the second call must echo it unchanged; the SDK never invents or
stores authorization. Success requires the native mutation, persistence,
independent absence/state readback, and cleanup terminal result. Invalid,
stale, or mismatched authorization fails before write.
