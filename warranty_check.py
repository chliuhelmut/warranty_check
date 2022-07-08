
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import configparser
import os
import time


class warranty_check(object):


    def __init__(self):
        
        self.settings=configparser.ConfigParser()
        self.settings.read(os.path.join(os.getcwd() , 'conf', "warranty_page.conf"),encoding="utf-8")
        
  
    def warranty_input(self):
        self.browser=webdriver.Firefox()
        self.browser.get(self.settings.get('main','url_page'))
        print(self.settings.get("main","url_page"))
        print(self.settings.get("warranty_info","str_title"))
        #self.browser.find_element_by_xpath
    
    def warranty_hover(self):
        
        serial_box=self.browser.find_element_by_id(self.settings.get('id','serial'))
        ActionChains(self.browser).move_to_element(serial_box).perform()
        print(self.settings.get("warranty_info","str_title"))
        time.sleep(4)
        serial_box.click()
        #self.browser.find_element_by_xpath

    def close(self):
        img_file=os.path.join(os.getcwd() , 'img', "close.png")
        print(img_file)
        self.browser.get_screenshot_as_file(img_file)
        self.browser.close()




if __name__ == '__main__':
	
    check=warranty_check()
    check.warranty_input()
    check.warranty_hover()
    print(check.settings)
    check.close()
    
    