import strawberry
from .resolvers.server_type import resolve_server_types, resolve_server_types_db
from .resolvers.team_type import resolve_team_type, resolve_team_type_db

@strawberry.type
class Query:
    server_types = strawberry.field(resolver=resolve_server_types)
    team_type = strawberry.field(resolver=resolve_team_type)
    server_types_db = strawberry.field(resolver=resolve_server_types_db)
    team_type_db = strawberry.field(resolver=resolve_team_type_db)

