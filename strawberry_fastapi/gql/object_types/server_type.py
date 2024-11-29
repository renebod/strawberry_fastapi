import strawberry
from typing import List
from ..object_types.operating_system import OperatingSystem, OperatingSystemDB

@strawberry.type
class ServerType:
    key: str
    display_name: str
    operating_systems: List[OperatingSystem]
@strawberry.type
class ServerTypeDB:
    key: str
    display_name: str
    operating_systems: List[OperatingSystemDB]