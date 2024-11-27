import strawberry
from .resolvers.server_type import resolve_server_types
from .resolvers.team_type import resolve_team_type

@strawberry.type
class Query:
    server_types = strawberry.field(resolver=resolve_server_types)
    team_type = strawberry.field(resolver=resolve_team_type)

