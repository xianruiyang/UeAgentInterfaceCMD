"""Exact, projection-only bindings for T38 modeling geometry operations."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class ModelingGeometryBinding:
    command_id: str
    contract_hash: str


COMMAND_IDS = (
    "mesh.attribute.material_slot.add",
    "mesh.attribute.material_slot.assign",
    "mesh.attribute.normals.recompute",
    "mesh.attribute.uv.auto",
    "mesh.attribute.uv.project",
    "mesh.collision.convex.generate",
    "mesh.collision.simple.generate",
    "mesh.primitive.box.create",
    "mesh.primitive.cylinder.create",
    "mesh.primitive.plane.create",
    "mesh.primitive.ramp.create",
    "mesh.primitive.ramp_corner.create",
    "mesh.primitive.sphere.create",
    "mesh.primitive.stairs.create",
    "mesh.topology.boolean",
    "mesh.topology.edges.bevel",
    "mesh.topology.edges.weld",
    "mesh.topology.faces.duplicate",
    "mesh.topology.faces.extrude",
    "mesh.topology.faces.inset",
    "mesh.topology.faces.offset",
    "mesh.topology.faces.push_pull",
    "mesh.topology.holes.fill",
    "mesh.topology.mesh_cut",
    "mesh.topology.mirror",
    "mesh.topology.plane_cut",
    "mesh.topology.remesh",
    "mesh.topology.simplify",
    "mesh.topology.subdivide",
    "mesh.topology.trim",
    "mesh.topology.voxel_boolean",
)


_CONTRACT_HASHES = {
    "mesh.attribute.material_slot.add": "sha256:bad949b043ab19563631b1bfcce50e08ef23db4aa51a7068d60b4f9deb23e956",
    "mesh.attribute.material_slot.assign": "sha256:9cf33c547e9e2e1eec4a70eb3b349b5e664c3a94dae26ccc6f1918180a6e399a",
    "mesh.attribute.normals.recompute": "sha256:10d25959aea5e2825a180662e9cbc5711395e8fd7dbc0b095b89730af425c51f",
    "mesh.attribute.uv.auto": "sha256:71b5dd0321c54fe0b66209ec2dd8565c76ce9c53507d1510e531f0fee7972261",
    "mesh.attribute.uv.project": "sha256:012ffb197dd1f304cba5baba82018c86e02a619d48a8004e9091f9e905b6d845",
    "mesh.collision.convex.generate": "sha256:848f0b968860fd4f758634f0cfa3d981fb4253a5df297cda648f0a75560fd4d8",
    "mesh.collision.simple.generate": "sha256:7f43d8d7f7cd5f2eed04fc2ef0248e32427fe0e8153cf09a32d25a3d7b0fed96",
    "mesh.primitive.box.create": "sha256:b672c51b44985fb202a7290c8932d7cfd575802b78c033c315e03fee3af787a0",
    "mesh.primitive.cylinder.create": "sha256:555401bb94dd07ea15d3336579d68adbe60ae4090a0757feac8f86c4340a7b6f",
    "mesh.primitive.plane.create": "sha256:3ab9beb3ecaa76885d8f636ca938a3ebbc921d23da645ad4b0149f6515847a71",
    "mesh.primitive.ramp.create": "sha256:7f07f19d7af37a97ed86b202fb7bbc479119c1a05f3ea285231513713da4fe5d",
    "mesh.primitive.ramp_corner.create": "sha256:896b1261a8a29a0ef192c877087458860df4a872040378b3300e508fbdf759e7",
    "mesh.primitive.sphere.create": "sha256:f928d3c97eb154036339deda31b0fe5b7753e7a498730aae8ecdf2f5b6bf3f96",
    "mesh.primitive.stairs.create": "sha256:a76c176c7e2960d86539be02194041b3d1c45a3df44ba3ca0007c85cee4d7f8d",
    "mesh.topology.boolean": "sha256:fda96d8e98a4ffb5faa5081dc76e91ad029da4f9b93d4c02637e4623aee4d890",
    "mesh.topology.edges.bevel": "sha256:58ae213a222d2aa6873ebfc688bbc4638ea60fd5f9330d7b649e855ca7de0723",
    "mesh.topology.edges.weld": "sha256:67a6b235a43a070fd157139a6a1e0aca4ee5071af59e00bc8b29d3ca5a19a583",
    "mesh.topology.faces.duplicate": "sha256:5233a7d4b4bbacd0bb8f924fdc5e9b737a7a9ebc0240b440186abc454334c590",
    "mesh.topology.faces.extrude": "sha256:411c9f44fd6d3458f3a2fb15f2f6d3732c5f05b1ec1bc077c2e7e67ea364d461",
    "mesh.topology.faces.inset": "sha256:5b088b63b265ec7d4783ec14cada9eab54cf8f5c8c8d6d468e35cf59de5c5270",
    "mesh.topology.faces.offset": "sha256:5717d254da62d330d363362cb8dfaa0f68216504173fef7ef58ece5f91b5af2a",
    "mesh.topology.faces.push_pull": "sha256:933912b5179965220b157647454b364ed07a3a6cb0b222751426fe9fc52ca2a5",
    "mesh.topology.holes.fill": "sha256:739a22ff1156873b466d29cbd6a24b846acd2b38431c3a8b9b8342c49eba4cbc",
    "mesh.topology.mesh_cut": "sha256:831375065f3e0ee016bac8de599995070d418efe95f2e44c35ccce01d9e25b11",
    "mesh.topology.mirror": "sha256:010cd4be1b7e7a97ea839ccaaab018102b539e12876dd4ff17017afbbaba0616",
    "mesh.topology.plane_cut": "sha256:6fd87585a2327b0efd9f9c7dbf6a8f26105b8d6c62238352b14798eab141aa1e",
    "mesh.topology.remesh": "sha256:54c6a0f8efde86f6c33114f68b5b04d4953ce626ffb5c86f513f5056e9b11382",
    "mesh.topology.simplify": "sha256:c9af78ce98b2f14d2490b84e075ba4fb0e9e94c6cf325823e161a5fd95595dae",
    "mesh.topology.subdivide": "sha256:6727ee4d2f1fbb012323e67b6ec64a69baa9728188895b9623d87186dc51b051",
    "mesh.topology.trim": "sha256:76f5e5d5ec623d6b1a460584eab621747ccd682c4440adf1ad620aa000572e70",
    "mesh.topology.voxel_boolean": "sha256:09851ed6fd88a007b1f6721da93f11cb13ce20fc8cd05a00fe9c8dd7f9562bd3",
}
BINDINGS = MappingProxyType(
    {
        command_id: ModelingGeometryBinding(command_id, _CONTRACT_HASHES[command_id])
        for command_id in COMMAND_IDS
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS.get(command_id)
    if binding is None:
        raise ValueError(f"modeling_geometry_command_unknown: {command_id}")
    return client.execute_exact(
        binding.command_id,
        params,
        contract_hash=binding.contract_hash,
    )


__all__ = ["BINDINGS", "COMMAND_IDS", "ModelingGeometryBinding", "execute"]
