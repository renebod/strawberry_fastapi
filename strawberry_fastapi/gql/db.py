import couchdb
import os 

class Couch:
    def __init__(self,database:str='reference_objects') -> None:
        self.username = os.environ.get('COUCHDB_USERNAME', 'admin')
        self.password = os.environ.get('COUCHDB_PASSWORD', 'admin')
        self.dbhost =  os.environ.get('COUCHDB_HOSTNAME', '127.0.0.1')
        self.port = os.environ.get('COUCHDB_PORT', '5984')
        self.database_to_fetch = database
        self.databases = ['functional_objects', 'technical_objects', 'reference_objects', 'reference_schema']
        self.couchserver = couchdb.Server(f"http://{self.username}:{self.password}@{self.dbhost}:{self.port}/")
        self.__populate_server()
    
    def __populate_server(self):
        for db in self.databases:
            if db in self.couchserver:
                pass
            else:
                self.couchserver.create(db)

    def get_database(self):
        # Assuming data exists we already accessing data
        # Need a try catch or better logic here
        if self.database_to_fetch in self.couchserver:
            return self.couchserver[self.database_to_fetch]
        else:
            print(f'Database does not exit {self.database_to_fetch}')
            return 
            
    
    def save_item(self):
        pass 

    def delete_item(self):
        pass
