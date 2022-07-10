import pytest
from selenium import webdriver
import configparser
import os

settings=configparser.ConfigParser()
settings.read(os.path.join(os.getcwd() , 'conf', "warranty_page.conf"),encoding="utf-8")


@pytest.fixture(scope='class')
def web_init(request):
    web=webdriver.Firefox()
    request.cls.driver=web
    web.implicitly_wait(10)
    #app.get(settings.get("main","url_page"))
    yield
    web.close()