

import os
import time
import configparser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import sys
#sys.path.append(os.path.join(os.getcwd() ,'..'))
import pytest
from sqlalchemy import true

class test_warranty(object):

    def __init__(self):
        
        self.testdata=configparser.ConfigParser()
        self.testdata.read(os.path.join(os.getcwd() , 'test', "warranty_testdata.conf"),encoding="utf-8")
        self.settings=configparser.ConfigParser()
        self.settings.read(os.path.join(os.getcwd() , 'conf', "warranty_page.conf"),encoding="utf-8")
    
    def warranty_page(self):
        self.app=webdriver.Firefox()
        self.app.get(self.settings.get('main','url_page'))
        
    
    def warranty_element(self,element_id):
        return self.app.find_element_by_id(element_id)

    def test_page(self):
        id=self.settings.get('id','serial')
        #self.app.warranty_check()
        assert id == 'SerialNumber' 
        


if __name__ == '__main__':
	
    check=test_warranty()
    check.warranty_page()
    check.test_page()
    #check.warranty_hover()
    print(check.settings)
    #check.close()
    