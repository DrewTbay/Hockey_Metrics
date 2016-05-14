from hockeyrefselenium import HockeyReferenceGarther
from dbconn import PostgresConnection

driver = HockeyReferenceGarther()

driver.RecursiveIterationThroughTableLinks \
    ("http://www.hockey-reference.com/teams/", \
    "active_franchises")
    
print ("Attempting to connect to database...")
#connect the the database using the the attached ConfigFile
database_connection = PostgresConnection('config\iniPostgres.ini')

driver.close()
