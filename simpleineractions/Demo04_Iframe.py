from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.rediff.com/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.delete_all_cookies()

print(driver.find_element_by_xpath("//div[@id='topdiv_0']//h2[@class='news'][1]/a").text)

#Switch to frame using index
driver.switch_to.frame(0)
print(driver.find_element_by_xpath("//span[@id='bseindex']").text)
#Switch back to parent html
driver.switch_to.parent_frame()
print(driver.find_element_by_xpath("//div[@id='topdiv_0']//h2[@class='news'][2]/a").text)

#Switch to frame using name or id
driver.switch_to.frame("moneyiframe")
print(driver.find_element_by_xpath("//span[@id='nseindex']").text)
#Switch back to parent html
driver.switch_to.default_content()
print(driver.find_element_by_xpath("//div[@id='topdiv_0']//h2[@class='news'][3]/a").text)

#Switch to frame using frame webelement
driver.switch_to.frame(driver.find_element_by_id("moneyiframe"))
print(driver.find_element_by_xpath("//span[@id='NseChange']").text)
#Switch back to parent html
driver.switch_to.default_content()
print(driver.find_element_by_xpath("//div[@id='topdiv_0']//h2[@class='news'][4]/a").text)

driver.quit()


