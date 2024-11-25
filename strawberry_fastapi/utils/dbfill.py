import db
from uuid import uuid4


databases = ['functional_objects', 'technical_objects', 'reference_objects']

ref_db = db.get_database('reference_objects')

for ref in [
        {'name': 'windows 11 server', 'ref_type': 'server_type'},
        {'name': 'windows 10 server', 'ref_type': 'server_type'},
        {'name': 'windows xp server', 'ref_type': 'server_type'},
        {'name': 'linux server', 'ref_type': 'server_type'},
        {'name': 'osx server', 'ref_type': 'server_type'},

        {'name': 'marketing support team', 'ref_type': 'team_type'},
        {'name': 'sales support team', 'ref_type': 'team_type'},
        {'name': 'tech support team', 'ref_type': 'team_type'},
        {'name': 'housing support team', 'ref_type': 'team_type'},
        {'name': 'management support team', 'ref_type': 'team_type'},
        {'name': 'research support team', 'ref_type': 'team_type'},
        {'name': 'cleaning support team', 'ref_type': 'team_type'},
    ]:
    ref['_id'] = str(uuid4())
    ref_db.save(ref)