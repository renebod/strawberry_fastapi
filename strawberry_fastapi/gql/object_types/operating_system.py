import strawberry

@strawberry.type
class OperatingSystem:
    key: str
    display_name: str


@strawberry.type
class OperatingSystemDB:
    key: str
    display_name: str
    ref_type: str
    server_type: str
