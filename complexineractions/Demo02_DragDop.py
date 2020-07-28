from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://jqueryui.com/resources/demos/droppable/default.html")
driver.set_page_load_timeout(10)

from_drag=driver.find_element_by_xpath("//div[@id='draggable']")
to_drag=driver.find_element_by_xpath("//div[@id='droppable']")

actions=ActionChains(driver)
actions.drag_and_drop(from_drag,to_drag).perform()

driver.refresh()
actions=ActionChains(driver)
from_drag=driver.find_element_by_xpath("//div[@id='draggable']")
to_drag=driver.find_element_by_xpath("//div[@id='droppable']")
actions.click_and_hold(from_drag).move_to_element(to_drag).release().perform()