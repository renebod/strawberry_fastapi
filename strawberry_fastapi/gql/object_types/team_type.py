import strawberry

@strawberry.type
class TeamType:
    key: str
    display_name: str
@strawberry.type
class TeamTypeDB:
    key:str
    name: str