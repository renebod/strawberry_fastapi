import strawberry
from .resolvers.server_type import resolve_server_types_db #,resolve_server_types, 
from .resolvers.team_type import resolve_team_type_db #.resolve_team_type, 

@strawberry.type
class Query:
    # server_types = strawberry.field(resolver=resolve_server_types)
    # team_type = strawberry.field(resolver=resolve_team_type)
    server_types_db = strawberry.field(resolver=resolve_server_types_db)
    team_type_db = strawberry.field(resolver=resolve_team_type_db)

