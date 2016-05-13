from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://www.hockey-reference.com/teams/")

assert "Python" in driver.title

# Find the table that lists all of the active franchises for Hockey.
# Yes I know this is canadian as it sounds :P
activeFran = driver.find_element_by_name("active_franchises")

print activeFran.size()

assert "No results found." not in driver.page_source

driver.close()
