# import db
import couchdb
import os
from uuid import uuid4


username = os.environ.get('COUCHDB_USERNAME', 'admin')
password = os.environ.get('COUCHDB_PASSWORD', 'password')
dbhost =  os.environ.get('COUCHDB_HOSTNAME', 'couchdb')
port = os.environ.get('COUCHDB_PORT', '5984')
couchserver = couchdb.Server(f"http://{username}:{password}@{dbhost}:{port}/")


def get_database(db_name):
    return couchserver[db_name]

databases = ['functional_objects', 'technical_objects', 'reference_objects']

for database in databases:
        if database in couchserver:
            db = couchserver[database]
        else:
            db = couchserver.create(database)

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