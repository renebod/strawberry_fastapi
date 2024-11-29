from ..object_types.team_type import TeamType, TeamTypeDB
from ..db import Couch

# need to find common way to not open multiple connection to database
couchserver = Couch()
db = couchserver.get_database()

def resolve_team_type(key: str) -> TeamType:
    mock_teams = {
        "dev": TeamType(key="dev", display_name="Development Team"),
        "qa": TeamType(key="qa", display_name="QA Team"),
        "ops": TeamType(key="ops", display_name="Operations Team"),
    }
    return mock_teams.get(key, TeamType(key="unknown", display_name="Unknown Team"))

def resolve_team_type_db(key: str) -> list[TeamTypeDB]:
    mango = {'selector': {'ref_type':'team_type', 'key':{'$regex': f'.*{key}.*'}}}
    result = db.find(mango_query=mango) 
    data =[]
    for entry in result:
        data.append(TeamTypeDB(key=entry['key'],name=entry['name']))
    return data