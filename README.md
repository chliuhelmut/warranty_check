# warranty_check

## [Dependecy] 

*selenium
*configparser
*pytest
*pytest-html
*Webdriver binary(firefox,chrome)


## [Main]

參考Page Object Model,開發一個簡化的 Web UI automation test suite.
利用 Pytest 的 test suite 與 Pytest-html的輸出測試報告

*開發者需針對測試網頁 頁面的功能及元件操作
*測試者需開發測試網頁的測試案例
*測試錯誤是有Pytest report 也可以同時輸出screenshot方便確認UI 的問題


## 擴展性

*將網頁的基本元素及selector，待驗字串等，獨立一個settings config file
*測試資料 也與測試案例分離 分別存放於 testdata config file

在頁面修改或測試項目增加時可以無需大改library 可以快速新增所需的測試場景


## Structure

root
|
---/test : test data config file
|   
---/conf : test target config file
|   
---/tools : binary tools of webdriver
