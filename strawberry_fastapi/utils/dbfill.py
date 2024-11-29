# import db
import couchdb
import os
from uuid import uuid4


username = os.environ.get('COUCHDB_USERNAME', 'admin')
# password = os.environ.get('COUCHDB_PASSWORD', 'password')
password = os.environ.get('COUCHDB_PASSWORD', 'admin') #using local installed couchdb
# dbhost =  os.environ.get('COUCHDB_HOSTNAME', 'couchdb')
dbhost =  os.environ.get('COUCHDB_HOSTNAME', '127.0.0.1') #using local installed couchdb
port = os.environ.get('COUCHDB_PORT', '5984')
couchserver = couchdb.Server(f"http://{username}:{password}@{dbhost}:{port}/")
# couchserver = couchdb.Server(f"http://admin:admin@127.0.0.1:5984/")
databases = ['functional_objects', 'technical_objects', 'reference_objects', 'reference_schema']

def get_database(db_name, couchserver=couchserver):
    return couchserver[db_name]


def initalise_dbs(databases=databases, couchserver=couchserver):
    for database in databases:
            if database in couchserver:
                # db = couchserver[database]
                pass
            else:
                # db = couchserver.create(database)
                couchserver.create(database)
    return 

def populate_ref_object_data(update:bool=False):
    ref_db = get_database('reference_objects')
    if not update:
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
    else:
         print('Update DB')
         for ref in [
            #   Update for team entries
            #   {'key':'dev', 'name': 'Development Team', 'ref_type':'team_type'},
            #   {'key':'qa', 'name': 'QA Team', 'ref_type':'team_type'},
            #   {'key':'ops', 'name': 'Operations Team', 'ref_type':'team_type'},
            #   {'key':'business', 'name': 'Business Team', 'ref_type':'team_type'},
            # Update for nested entries
            {'key': '', 'dsiplay_name': '', 'ref_type': 'server_type','operating_systems':[
                 {'key':'', 'display_name':'', 'ref_type': 'os_type'}
            ]},
            {'key': '', 'dsiplay_name': '', 'ref_type': 'server_type','operating_systems':[
                 {'key':'', 'display_name':'', 'ref_type': 'os_type'}
            ]},
            {'key': '', 'dsiplay_name': '', 'ref_type': 'server_type','operating_systems':[
                 {'key':'', 'display_name':'', 'ref_type': 'os_type'}
            ]},
            {'key': '', 'dsiplay_name': '', 'ref_type': 'server_type','operating_systems':[
                 {'key':'', 'display_name':'', 'ref_type': 'os_type'}
            ]},
            {'key': '', 'dsiplay_name': '', 'ref_type': 'server_type','operating_systems':[
                 {'key':'', 'display_name':'', 'ref_type': 'os_type'}
            ]},
            {'key': '', 'dsiplay_name': '', 'ref_type': 'server_type','operating_systems':[
                 {'key':'', 'display_name':'', 'ref_type': 'os_type'}
            ]},
         ]:
              ref['_id'] = str(uuid4())
              ref_db.save(ref)


if __name__ == '__main__':
    print('hello world')
    # populate_ref_object_data(update=True)

