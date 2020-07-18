from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver= webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://reminderbot.io/")
print("Title is "+driver.title)
driver.minimize_window()
print("Current Url is "+driver.current_url)
driver.maximize_window()
driver.quit()



