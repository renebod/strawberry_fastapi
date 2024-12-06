import strawberry
from typing import List
from ..object_types.operating_system import OperatingSystem #, OperatingSystemDB
from ..resolvers.operating_system import resolve_operating_system_db #, resolve_operatings_system_server_type_db

@strawberry.type
class ServerType:
    key: str
    display_name: str
    operating_systems: List[OperatingSystem]
@strawberry.type
class ServerTypeDB:
    key: str
    display_name: str
    operating_systems= strawberry.field(resolver=resolve_operating_system_db)
    
    # Attempt to have nested fields
    # operating_systems : List[OperatingSystemDB]   
    # @strawberry.field
    # def operating_systems(self, info: strawberry.Info):
    #     # Does not work as it still requires input of server_type
    #     resolver_chain = [
    #       resolve_operating_system_db,
    #       resolve_operatings_system_server_type_db
    #    ]
        
    #     # Call the resolver chain
    #     data = info.context["resolver_chain"](self.key,resolver_chain)
    #     return data()
        
