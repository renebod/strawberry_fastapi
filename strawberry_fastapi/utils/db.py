import couchdb
import os

# from handlers.exception import BadRequestException

async def init_databases(databases):
    global couchserver
    username = os.environ.get('COUCHDB_USERNAME', 'admin')
    password = os.environ.get('COUCHDB_PASSWORD', 'password')
    dbhost =  os.environ.get('COUCHDB_HOSTNAME', 'couchdb')
    port = os.environ.get('COUCHDB_PORT', '5984')
    couchserver = couchdb.Server(f"http://{username}:{password}@{dbhost}:{port}/")

    for database in databases:
        if database in couchserver:
            db = couchserver[database]
        else:
            db = couchserver.create(database)

def get_database(name):
    return couchserver[name]

# def save_object(database, template, object):
#     '''
#     Placeholder for centralized DB save actions
#     '''
#     couch_database = get_database(database)
#     return couch_database.save(object)

# def save_technical_object(tech_obj):
#     couch_database = get_database('technicals')

#     # Get Current Technical Object for comparison 
#     current_tech_obj = couch_database.get(tech_obj.get('_id'))

#     # Pop all the keys of the technical object to be saved, but store the values for after the comparison
#     tech_updated_at = tech_obj.pop('updated_at', None)

#     # Compare if there are uncommitted changes, true if object does not already exist
#     if current_tech_obj:
#         if tech_obj['_rev'] != current_tech_obj['_rev']:
#             raise BadRequestException(message=f"Wrong document revision provided. Make sure your _rev matches {current_tech_obj['_rev']}.")

#         # Pop all the not to be compared keys from the current technical object
#         current_tech_obj.pop('uncommitted_change', None)
#         current_tech_obj.pop('updated_at', None)

#         tech_obj['uncommitted_change'] = {**current_tech_obj} != {**tech_obj}
#     else:
#         tech_obj['uncommitted_change'] = True

#     # Place back the popped keys from the rendered technical object
#     tech_obj['updated_at'] = tech_updated_at

#     return couch_database.save(tech_obj)

# def save_functional_object(func_obj):
#     couch_database = get_database('functionals')
#     return couch_database.save(func_obj)