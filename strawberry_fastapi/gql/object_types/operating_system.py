import strawberry

@strawberry.type
class OperatingSystem:
    key: str
    display_name: str