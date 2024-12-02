from ..object_types.operating_system import OperatingSystemDB
from ..db import Couch

# need to find common way to not open multiple connection to database
couchserver = Couch()
db = couchserver.get_database()

def resolve_operatings_system_server_type_db(server_type:str)-> list[OperatingSystemDB]:
    mango = {'selector': {'ref_type':'os_type', 'server_type':{'$regex': f'.*{server_type}.*'}}}
    result = db.find(mango_query=mango) 
    data =[]
    for entry in result:
        data.append(OperatingSystemDB(key=entry['key'],display_name=entry['display_name'], ref_type=entry['ref_type'], server_type=entry['server_type']))
    return data


def resolve_operating_system_db(key: str) -> list[OperatingSystemDB]:
    mango = {'selector': {'ref_type':'os_type', 'key':{'$regex': f'.*{key}.*'}}}
    result = db.find(mango_query=mango) 
    data =[]
    for entry in result:
        data.append(OperatingSystemDB(key=entry['key'],display_name=entry['display_name'], ref_type=entry['ref_type'], server_type=entry['server_type']))
    return data