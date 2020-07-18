from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.jqueryscript.net/demo/jQuery-Plugin-For-Filterable-Bootstrap-Dropdown-Select-Bootstrap-Select/")
driver.implicitly_wait(30)
driver.maximize_window()

button=driver.find_element_by_id("bts-ex-1")
button.click()
all_options=button.find_elements_by_class_name("items")
try:
    print(driver.find_element_by_xpath("//span[class='text]").text)
except NoSuchElementException as ex:
    print("Element is not selected")
print(len(all_options))

for webelement in all_options:
    if webelement.text=="Item 2":
        webelement.click()
        break
print(driver.find_element_by_xpath("//span[@class='text']").text)

driver.quit()