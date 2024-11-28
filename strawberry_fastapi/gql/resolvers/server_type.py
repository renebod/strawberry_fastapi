from ..object_types.server_type import ServerType
from ..object_types.operating_system import OperatingSystem
 
def resolve_server_types() -> list[ServerType]:
    # name
    # var ='win'
    # mango = {'selector': {'ref_type':'server_type', 'name':{'$regex': f'.*{name}.*'}},'fields':['name']}
    return [
        ServerType(
            key="windows",
            display_name="Windows Server",
            operating_systems=[
                OperatingSystem(key="windows-server-2012", display_name="Windows Server 2012"),
                OperatingSystem(key="windows-core-server-2023", display_name="Windows Core Server 2023"),
            ],
        ),
        ServerType(
            key="redhatlinux",
            display_name="Red Hat Linux",
            operating_systems=[
                OperatingSystem(key="redhat-linux-enterprise-2022", display_name="Red Hat Linux Enterprise 2022"),
            ],
        ),
        ServerType(
            key="oraclelinux",
            display_name="Oracle Linux",
            operating_systems=[
                OperatingSystem(key="oracle-linux-2023", display_name="Oracle Linux 2023"),
            ],
        ),
    ]