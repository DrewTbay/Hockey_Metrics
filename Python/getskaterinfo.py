from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dbconn import PostgresConnection

driver = webdriver.Firefox()

driver.get("http://www.hockey-reference.com/teams/")

activeFran = driver.find_element_by_name("active_franchises")
print(activeFran)

trs = driver.find_elements(By.id, "active_franchises") 
tds = trs[1].find_elements(By.TAG_NAME, "td")
#print(tds)
    
print ("Attempting to connect to database...")
#connect the the database using the the attached ConfigFile
database_connection = PostgresConnection('config\iniPostgres.ini')

driver.close()