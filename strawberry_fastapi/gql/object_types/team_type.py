import strawberry

@strawberry.type
class TeamType:
    key: str
    display_name: str