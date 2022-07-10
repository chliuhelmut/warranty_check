
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import os
import time


class warranty_check(object):


    def __init__(self,driver):
                
        self.browser=driver
        self.settings=configparser.ConfigParser()
        self.settings.read(os.path.join(os.getcwd() , 'conf', "warranty_page.conf"),encoding="utf-8" )
        self.browser.get(self.settings.get('main','url_page'))
        

    def cookie_confirm(self):
        
        self.cookies_confirm=self.browser.find_element_by_id('onetrust-accept-btn-handler')
        self.cookies_confirm.click()   
        

    def get_warranty_title(self):
        return self.browser.title
        
        
    def warranty_hover(self,locator):
        self.elem=WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(locator))
        ActionChains(self.browser).move_to_element(self.elem).perform()
        time.sleep(4)
        
    
    def get_warranty_element(self,locator):
        try:
            self.elem=WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(locator))
            return self.elem
        except TimeoutException:
            return None
            
        
    

    def warranty_click(self,locator):
        
        self.elem=WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(locator))
        self.elem.click()

    def warranty_setkey(self,locator,key):
        
        self.elem=WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(locator))
        self.elem.send_keys(key)

    def warranty_clearkey(self,locator):
        
        self.elem=WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(locator))
        self.elem.clear()
    
    def get_element_attr(self,attr):
        
        if attr in ('font-family','color','background-color','border-bottom-color','display'):
            
            self.elem_attr=self.elem.value_of_css_property(attr)
            return self.elem_attr

    def get_element_text(self):
        
        return self.elem.text
        

    def get_screenshot(self,filename):
        self.browser.save_screenshot(filename)


    


if __name__ == '__main__':
	
    pass
    
    