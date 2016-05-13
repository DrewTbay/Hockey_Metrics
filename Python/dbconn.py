
""""
By: Drew Reid
Date: May 8,2016
Purpose: 
    class to make connection to postgres
"""

from dbconfig import DatabasePostgresConfig

import psycopg2

class PostgresConnection:


    _database_connection = None
    
    """Constructor of the database Connection.
        Pass in the location of the configure file for the database.
        Set the _database_connection to the cussor of the postgres database
    """
    def __init__(self, configure_file):
        try:
            database_config_info = DatabasePostgresConfig(configure_file)
            database_login_info \
                = database_config_info.ReadDatabaseConnection()
            postgres_login \
                = psycopg2.connect(**database_login_info)
            self._database_connection = postgres_login.cursor()
        except psycopg2.DatabaseError as e: 
            print ('Error %s' % e )
            sys.exit(1)
			
    """
    """
    def QueryDatabase(self, query):
        try:
            return self._database_connection.execute(query)
        except psycopg2.DatabaseError as e: 
            print(e)
	
    def QueryDatabaseWithParams(self, query, params):
        try:
            return self._database_connection.execute(query)
        except psycopg2.DatabaseError as e: 
            print(e)
    
    def __del__(self):
        self._database_connection.close()