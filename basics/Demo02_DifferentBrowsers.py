from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#driver= webdriver.firefox(executable_path="GeckoDriver.exe")
driver= webdriver.firefox(GeckoDriverManager.install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://reminderbot.io/")
print("Title is "+driver.title)
driver.minimize_window()
print("Current Url is "+driver.current_url)
driver.maximize_window()
driver.quit()

#driver= webdriver.edge(executable_path="MicrosoftWebDriver.exe")
driver= webdriver.edge(EdgeChromiumDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://reminderbot.io/")
print("Title is "+driver.title)
driver.minimize_window()
print("Current Url is "+driver.current_url)
driver.maximize_window()
driver.quit()



