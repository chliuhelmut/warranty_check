

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


class Test_warranty(test_web):
    
   
    def test_setup(self):
        self.page=warranty_check(self.driver)
        self.page.cookie_confirm()
        

    def test_warranty_page(self):
        
        self.page=warranty_check(self.driver)
        
        assert bool(self.page.get_warranty_title()) , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "warranty_title.png"))
        
    
    def test_warranty_info_text(self):
        
        self.page=warranty_check(self.driver)
        #self.page.get_warranty_element((By.ID,settings.get('id','serial')))
        self.page.warranty_setkey((By.ID,settings.get('id','serial')),testdata.get('warranty_serial','serial_number'))
        self.page.warranty_click((By.CSS_SELECTOR,settings.get('css','button')))
        #self.page.element_click(testdata.get('warranty_info','serial_number'))
        list_text=[]
        list_expect=[]
        for i in range(6):
            xpath_pre="/html/body/div[1]/div[2]/section/div/div[2]/div/div/div/div/div[2]/dt["+ str(i+1) +"]"
            self.elem=self.page.get_warranty_element((By.XPATH,xpath_pre))
            info_str=self.page.get_element_text()
            list_text.append(info_str)
            list_expect.append=settings.get('warranty_info','str_'+ str(i+1)) 

        assert list_text == list_expect , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "warranty_info_text.png"))
 
    def test_warranty_info_result(self):
        
        self.page=warranty_check(self.driver)
        
        self.page.warranty_setkey((By.ID,settings.get('id','serial')),testdata.get('warranty_serial','serial_number'))
        self.page.warranty_click((By.CSS_SELECTOR,settings.get('css','button')))
        
        list_text=[]
        list_expect=[]
        for i in range(6):
            xpath_pre="/html/body/div[1]/div[2]/section/div/div[2]/div/div/div/div/div[2]/dd["+ str(i+1) +"]"
            self.elem=self.page.get_warranty_element((By.XPATH,xpath_pre))
            info_str=self.page.get_element_text()
            list_text.append(info_str)
            list_expect.append=testdata.get('warranty_info','result_'+ str(i+1)) 

        assert list_text == list_expect , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "warranty_info_result.png"))

    def test_warranty_info_notfound(self):
        
        self.page=warranty_check(self.driver)
        
        self.page.warranty_setkey((By.ID,settings.get('id','serial')),testdata.get('warranty_serial','serial_number'))
        self.page.warranty_click((By.CSS_SELECTOR,settings.get('css','button')))
        
        list_text=[]
        list_expect=[]
                  
        self.elem=self.page.get_warranty_element((By.CLASS_NAME,settings.get('class','result_title')))
        info_str=self.page.get_element_text()
        list_text.append(info_str)
        
        result_expect=settings.get('warranty_info','str_title')+' '+ testdata.get('warranty_serial','serial_number')
        list_expect.append(result_expect) 
     


        assert list_text == list_expect , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "warranty_info_notfound.png"))

    def test_warranty_notfound_notice(self):
        
        self.page=warranty_check(self.driver)
        
        self.page.warranty_setkey((By.ID,settings.get('id','serial')),testdata.get('warranty_serial','serial_number'))
        self.page.warranty_click((By.CSS_SELECTOR,settings.get('css','button')))
                  
        self.elem=self.page.get_warranty_element((By.XPATH,settings.get('xpath','result_notfound_notice')))
        info_str=self.page.get_element_text()
       
        
        assert info_str == testdata.get('warranty_info','result_notice') , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "warranty_info_notice.png"))
        
