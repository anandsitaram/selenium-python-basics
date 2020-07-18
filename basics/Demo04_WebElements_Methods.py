from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
#driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver= webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://zero.webappsecurity.com/index.html")
driver.find_element(By.CLASS_NAME,"icon-signin").click()
driver.find_element(By.ID,"user_login").send_keys("username");
driver.find_element(By.NAME,"user_password").send_keys("password");
driver.find_element(By.NAME,"user_password").screenshot(os.getcwd()+"\\BeforeChange.png")
#clear()
driver.find_element(By.NAME,"user_password").clear()
driver.find_element(By.NAME,"user_password").screenshot(os.getcwd()+"\\AfterChange.png")

#submit() -Not working
#driver.find_element_by_name("submit").submit()
driver.find_element(By.NAME,"user_password").send_keys("password");
driver.find_element_by_name("submit").click()
print(driver.title)

#back()
driver.back()
print("After back "+driver.title)
#forward()
driver.forward()
print("After forward "+driver.title)

#refresh()
driver.refresh()
print("After refresh "+driver.title)

driver.get("http://testdiary.com/training/selenium/selenium-test-page")
print(driver.title)

#is_enabled() and is_selected()
print("Before enabled "+str(driver.find_element_by_id("demo").is_enabled()))
print("Before checked "+str(driver.find_element_by_id("java1").is_selected()))

driver.find_element_by_id("java1").click()
driver.find_element_by_id("demo").click()

print("After checked "+str(driver.find_element_by_id("java1").is_selected()))

#is_displayed
print("is_displayed "+str(driver.find_element_by_css_selector(".alert.blue").is_displayed()))

print(driver.find_element_by_css_selector(".alert.blue").text)

#size
dim=driver.find_element_by_css_selector(".alert.blue").size;
print(dim['height'])
print(dim['width'])


driver.quit()



