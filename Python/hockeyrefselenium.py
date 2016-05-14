from selenium import webdriver
import threading

class HockeyReferenceGarther:


    _web_driver = None
    
    def __init__(self):
        self._web_driver = webdriver.Firefox()
    
    def RecursiveIterationThroughTableLinks(self, url_link, table_id):
        self._web_driver.get(url_link)
        xpath = "//table[@id='" + table_id + "']//tr//td//a[1]"
        table_of_links = self._web_driver.find_elements_by_xpath(xpath)
        for link in table_of_links:
            link.click()
            exit
            #self._web_driver.back()
    
    def __del__(self):
        self._web_driver.close()
    