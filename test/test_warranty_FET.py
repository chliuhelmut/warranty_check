

import os
import time
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys
from pages.warranty_check import warranty_check
import pytest
from test.base_test import test_web
 

settings=configparser.ConfigParser()
settings.read(os.path.join(os.getcwd() , 'conf', "warranty_page.conf"),encoding="utf-8")
testdata=configparser.ConfigParser()
testdata.read(os.path.join(os.getcwd() , 'test', "warranty_testdata.conf"),encoding="utf-8")



class Test_warranty_fet(test_web):
    
   
    def test_setup(self):
        self.page=warranty_check(self.driver)
        self.page.cookie_confirm()
        #assert self.page.cookie_confirm()

     
  
    def test_serial_short(self):
        
        self.page=warranty_check(self.driver)
        self.page.warranty_setkey((By.ID,settings.get('id','serial')),testdata.get('warranty_serial','serial_number_short3'))
        self.page.warranty_click((By.CSS_SELECTOR,settings.get('css','button')))
        
        self.elem=self.page.get_warranty_element((By.CSS_SELECTOR,settings.get('css','style_field_short')))
        validation_str=self.page.get_element_text()
        

        assert validation_str == settings.get('validation_input','short_serial_number') , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "serial_short.png"))

    def test_serial_long(self):
        
        self.page=warranty_check(self.driver)
        
        self.page.warranty_setkey((By.ID,settings.get('id','serial')),testdata.get('warranty_serial','serial_number_long250'))
        self.page.warranty_click((By.CSS_SELECTOR,settings.get('css','button')))
        
        self.elem=self.page.get_warranty_element((By.CSS_SELECTOR,settings.get('css','style_field_invalid')))
        validation_str=self.page.get_element_text()
        

        assert validation_str == settings.get('validation_input','invalid_serial_number') , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "serial_long.png"))
   
    def test_serial_empty(self):
        
        self.page=warranty_check(self.driver)
        
        self.page.warranty_clearkey((By.ID,settings.get('id','serial')))
        self.page.warranty_click((By.CSS_SELECTOR,settings.get('css','button')))
        
        self.elem=self.page.get_warranty_element((By.CSS_SELECTOR,settings.get('css','style_field_empty')))
        validation_str=self.page.get_element_text()
        

        assert validation_str == settings.get('validation_input','no_serial_number') , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "serial_empty.png"))


    def test_serial_with_text(self):
        
        self.page=warranty_check(self.driver)
        
        self.page.warranty_setkey((By.ID,settings.get('id','serial')),testdata.get('warranty_serial','serial_number_text_1'))
        self.page.warranty_click((By.CSS_SELECTOR,settings.get('css','button')))
        
        self.elem=self.page.get_warranty_element((By.CSS_SELECTOR,settings.get('css','style_field_invalid')))
        validation_str=self.page.get_element_text()
        

        assert validation_str == settings.get('validation_input','invalid_serial_number') , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "serial_text.png"))

    def test_serial_with_special_char(self):
        
        self.page=warranty_check(self.driver)
        
        self.page.warranty_setkey((By.ID,settings.get('id','serial')),testdata.get('warranty_serial','serial_number_text_2'))
        self.page.warranty_click((By.CSS_SELECTOR,settings.get('css','button')))
        
        self.elem=self.page.get_warranty_element((By.CSS_SELECTOR,settings.get('css','style_field_invalid')))
        validation_str=self.page.get_element_text()
        

        assert validation_str == settings.get('validation_input','invalid_serial_number') , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "serial_char.png"))