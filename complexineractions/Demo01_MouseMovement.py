from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")
driver.set_page_load_timeout(15)

# Mouse Hover
mouse_hover = driver.find_element_by_id("nav-link-accountList")
actions = ActionChains(driver)
actions.move_to_element(mouse_hover).perform()
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Find a Gift']").click()
print("Mouse Hover Title is " + driver.title)

# Right click
actions = ActionChains(driver) # Initializing der again to avoid stale element exception
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
time.sleep(5)
rightClick = driver.find_element_by_xpath("//span[text()='right click me']")
actions.context_click(rightClick).perform()
rightClick_text=driver.find_element_by_xpath("//span[text()='Paste']")
print("Right Click text "+rightClick_text.text)
rightClick_text.click()

#Alert
print("Alert text "+driver.switch_to.alert.text)
driver.switch_to.alert.accept()

# Double click
doubletClick = driver.find_element_by_xpath("//button[text()='Double-Click Me To See Alert']")
actions.double_click(doubletClick).perform()
print("Alert Double text "+driver.switch_to.alert.text)
driver.switch_to.alert.accept()

driver.quit()






