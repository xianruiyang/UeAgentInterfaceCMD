"""Public entry package for the UAI remote client SDK.

Importing this package intentionally performs no I/O.
"""

from .errors import (
    Error,
    ProtocolError,
    SerializationError,
    ServerCommandError,
    TransportError,
    UsageError,
)
from .connection import connect
from .project_connection import connect_project
from .result import Result
from .operation import OperationHandle
from .runtime_session import RuntimeSessionHandle
from .pie import PieSession
from .asset_durable import DurableJournalHandle
from .artifact import ArtifactHandle
from .external_source import ExternalSourceNamespace, ProjectFileHandle
from .workspace import HjsonWorkspaceHandle, SceneAnalysisHandle
from .voxel_grid import VoxelGridHandle
from .rig_bake import RigBakeContextHandle
from .uai_client import Client
from .command_metadata import describe_command


__version__ = "0.4.0"

__all__ = [
    "__version__",
    "connect",
    "connect_project",
    "describe_command",
    "Client",
    "Result",
    "OperationHandle",
    "RuntimeSessionHandle",
    "PieSession",
    "DurableJournalHandle",
    "ArtifactHandle",
    "ExternalSourceNamespace",
    "HjsonWorkspaceHandle",
    "SceneAnalysisHandle",
    "ProjectFileHandle",
    "VoxelGridHandle",
    "RigBakeContextHandle",
    "Error",
    "UsageError",
    "SerializationError",
    "TransportError",
    "ProtocolError",
    "ServerCommandError",
]
