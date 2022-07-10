

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



class Test_warranty_ui(test_web):
    
   
    def test_setup(self):
        self.page=warranty_check(self.driver)
        self.page.cookie_confirm()
        #assert self.page.cookie_confirm()

    def test_warranty_page(self):
        #f.app=webdriver.Firefox()
        self.page=warranty_check(self.driver)
        #self.page.cookie_confirm()
        #webdriver_init.get(settings.get('main','url_page'))
        #print(settings.get('main','url_page'))
        assert bool(self.page.get_warranty_title()) 
        
    def test_warranty_id_font(self):
        
        self.page=warranty_check(self.driver)
        self.elem_id=self.page.get_warranty_element((By.ID,settings.get('id','serial')))
        self.elem_attr=self.page.get_element_attr('font-family')

        assert "museo-sans" in self.elem_attr , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "warranty_id_font.png"))
    
  
    def test_warranty_title(self):
        
        self.page=warranty_check(self.driver)
        self.elem=self.page.get_warranty_element((By.CLASS_NAME,settings.get('class','intro')))
        title_str=self.page.get_element_text()
        
        assert title_str == settings.get('warranty_input','title_warranty') , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "warranty_title_text.png"))

    def test_warranty_input_label(self):
        
        self.page=warranty_check(self.driver)
        self.elem=self.page.get_warranty_element((By.XPATH,settings.get('xpath','input_label')))
        label_str=self.page.get_element_text()
        
        assert label_str == settings.get('warranty_input','title_input_box') , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "warranty_input_label.png"))

    def test_warranty_button_label(self):
        
        self.page=warranty_check(self.driver)
        self.elem=self.page.get_warranty_element((By.CSS_SELECTOR,settings.get('css','button')))
        label_str=self.page.get_element_text()
        
        assert label_str == settings.get('warranty_input','button_name') , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "warranty_button_label.png"))

    def test_warranty_input_clicked(self):
        
        self.page=warranty_check(self.driver)
        #self.page.get_warranty_element((By.ID,settings.get('id','serial')))
        self.page.warranty_setkey((By.ID,settings.get('id','serial')),testdata.get('warranty_serial','serial_number'))
        self.elem_id=self.page.get_warranty_element((By.ID,settings.get('id','serial')))
        border_color=self.page.get_element_attr('border-bottom-color')
                  
        assert border_color == 'rgb(0, 0, 0)' , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "warranty_input_clicked.png"))


    def test_warranty_input_hover(self):
        
        self.page=warranty_check(self.driver)
        #self.page.get_warranty_element((By.ID,settings.get('id','serial')))
        self.page.warranty_hover((By.ID,settings.get('id','serial')))
        self.elem_id=self.page.get_warranty_element((By.ID,settings.get('id','serial')))
        border_width=self.page.get_element_attr('border-bottom-width')
                  
        assert border_width != '1px' , self.page.get_screenshot(os.path.join(os.getcwd() , 'img', "warranty_input_hover.png"))
