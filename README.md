# warranty_check


## [Introduction]

參考Page Object Model,開發一個簡化的 Web UI automation test suite.

利用 Pytest 的 test suite 與 Pytest-html的輸出測試報告

*開發者需針對測試網頁 頁面的功能及元件操作

*測試者需開發測試網頁的測試案例

*測試錯誤是有Pytest report 也可以同時輸出screenshot方便確認UI 的問題




## [擴展性]

*將網頁的基本元素及selector，待驗字串等，獨立一個settings config file

*測試資料 也與測試案例分離 分別存放於 testdata config file

在頁面修改或測試項目增加時可以無需大改library 可以快速新增所需的測試場景




## [Dependecy] 

Python modules and binary files used in this project

*selenium

*configparser

*pytest

*pytest-html

*Webdriver binary files (firefox,chrome - both for windows platform)




## [Structure]

root
|

---/test : stored test data config file

---/pages : stored web page library files    

---/conf : stored test target config file

---/test : stored test case library files of web pages and common pytest fixtures   

---/tools : binary tools of webdriver, currently supporting firefox and chrome 

---/img : stored screenshot png files of failed cases




## [Installation]

1. clone the project
2. install the dependecy modules via pip
3. export path of ./tools to env variable for launching executables
4. cd to project folder 
5. type "pytest -v" or "pytest -v --html=<report_name>.html" to launch the automation test
6. Pytest will discover the .py files with test prefix and start to perform testing.
7. screenshot png files will be stored under ./img folder if test failed in assertion




## [Test coverage]

### Function -  
            輸入測試serial number    檢查 warranty result    與預期結果 

            輸入不存在的serial number 檢查 warranty result   與錯誤提示
               

### FET  -      
            輸入過短的serial number 檢查 validation message

            輸入超過220字元的serial number 檢查 validation message
            
            未輸入serial number 檢查 validation message
            
            輸入有文字的serial number 檢查 validation message
            
            輸入特殊符號的serial number 檢查 validation message
            

### UI   -     
           檢查 warranty check title 字串

           檢查 warranty check page 字型family
           
           檢查 warranty input label 字串
           
           檢查 warranty button 字串
           
           檢查 warranty input box border color
           
           檢查 warranty input box hover border width
