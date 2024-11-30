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
            #   Update for team entries simple
            #   {'key':'dev', 'name': 'Development Team', 'ref_type':'team_type'},
            #   {'key':'qa', 'name': 'QA Team', 'ref_type':'team_type'},
            #   {'key':'ops', 'name': 'Operations Team', 'ref_type':'team_type'},
            #   {'key':'business', 'name': 'Business Team', 'ref_type':'team_type'},
            # Update for nested entries
            {'key': 'windows', 'display_name': 'Windows Server', 'ref_type': 'server_type','operating_systems':[
                 {'key':'windows-server-2012', 'display_name':'Windows Server 2012', 'ref_type': 'os_type'},
                 {'key':'windows-server-2019', 'display_name':'Windows Server 2019', 'ref_type': 'os_type'}
            ]},
            {'key': 'windows', 'display_name': 'Windows Server Core', 'ref_type': 'server_type','operating_systems':[
                 {'key':'windows-core-server-2023', 'display_name':'Windows Core Server 2023', 'ref_type': 'os_type'},
                 {'key':'windows-core-server-2020', 'display_name':'Windows Core Server 2020', 'ref_type': 'os_type'}
            ]},
            {'key': 'redhatlinux', 'display_name': 'Red Hat Linux', 'ref_type': 'server_type','operating_systems':[
                 {'key':'redhat-linux-enterprise-2022', 'display_name':'Red Hat Linux Enterprise 2022', 'ref_type': 'os_type'}
            ]},
            {'key': 'redhatlinux', 'display_name': 'Red Hat Linux', 'ref_type': 'server_type','operating_systems':[
                 {'key':'redhat-linux-enterprise-2020', 'display_name':'Red Hat Linux Enterprise 2020', 'ref_type': 'os_type'},
                 {'key':'redhat-linux-enterprise-2019', 'display_name':'Red Hat Linux Enterprise 2019', 'ref_type': 'os_type'}
            ]},
            {'key': 'oraclelinux', 'display_name': 'Oracle Linux', 'ref_type': 'server_type','operating_systems':[
                 {'key':'oracle-linux-2023', 'display_name':'Oracle Linux 2023', 'ref_type': 'os_type'},
                 {'key':'oracle-linux-2022', 'display_name':'Oracle Linux 2022', 'ref_type': 'os_type'}
            ]},
            {'key': 'oraclelinux', 'display_name': 'Oracle Linux', 'ref_type': 'server_type','operating_systems':[
                 {'key':'oracle-linux-2019', 'display_name':'Oracle Linux 2019', 'ref_type': 'os_type'}
            ]},
         ]:
              ref['_id'] = str(uuid4())
              ref_db.save(ref)


if __name__ == '__main__':
    print('hello world')
    # populate_ref_object_data(update=True)

