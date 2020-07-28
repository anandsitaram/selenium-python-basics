from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//a[text()='Multiple Windows']").click()
print("No of windows ",len(driver.window_handles))

driver.find_element_by_xpath("//a[text()='Click Here']").click()
print("No of windows ",len(driver.window_handles))
han=driver.window_handles
driver.switch_to.window(han[1])

print(driver.title)
driver.quit()

