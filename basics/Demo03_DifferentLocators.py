from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver= webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://zero.webappsecurity.com/index.html")
#class name
driver.find_element(By.CLASS_NAME,"icon-signin").click()
#id
driver.find_element(By.ID,"user_login").send_keys("username");
#name
driver.find_element(By.NAME,"user_password").send_keys("password");

#cssselector ->.classname( if there is a space add.)
driver.find_element(By.CSS_SELECTOR,".btn.btn-primary").click()
print(driver.title)
driver.get_screenshot_as_file("Test.png")
driver.quit()



