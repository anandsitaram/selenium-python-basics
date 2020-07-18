from datetime import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


start_time = time.time()
driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app.hubspot.com/login")

#impilict wait
driver.implicitly_wait(10)

driver.maximize_window()
driver.find_element_by_id("username").send_keys("testwebclient191@gmail.com")
driver.find_element_by_id("password").send_keys("TeSt@123")
driver.find_element_by_id("loginBtn").click()
driver.find_element_by_xpath("//span[contains(text(),'Service')]").click()
driver.find_element_by_xpath("//h4[contains(text(),'Customer Question')]").click()
print(driver.find_element_by_xpath("//i18n-string[@data-key='dashboard-actions.createDashboard.title']").text)
driver.find_element_by_xpath("//div[@role='button']").click()
driver.find_element_by_id("nav-primary-conversations-branch").click()
driver.find_element_by_id("nav-secondary-inbox").click()
print(driver.find_element_by_xpath("//i18n-string[@data-key='conversations-inbox-ui.zero-state.connectNewChannel.title']").text)

driver.find_element(By.ID,"account-menu").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Sign ").click()
print(driver.title)
print("--- %s seconds ---" % (time.time() - start_time))


driver.quit()