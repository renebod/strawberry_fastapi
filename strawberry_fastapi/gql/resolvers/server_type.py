from ..object_types.server_type import ServerType, ServerTypeDB
from ..db import Couch
from ..object_types.operating_system import OperatingSystem, OperatingSystemDB

# need to find common way to not open multiple connection to database
couchserver = Couch()
db = couchserver.get_database()
 
def resolve_server_types() -> list[ServerType]:
    # Mocked values
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

def resolve_server_types_db(name:str)-> list[ServerTypeDB]:
    mango = {'selector': {'ref_type':'server_type', 'key':{'$regex': f'.*{name}.*'}}}

    result = db.find(mango_query=mango)
    data =[]
    for entry in result:
        data.append(ServerTypeDB(key=entry['key'], display_name=entry['display_name']))
    return data 

