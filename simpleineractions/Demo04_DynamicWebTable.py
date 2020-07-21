from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://classic.freecrm.com/index.html")
driver.implicitly_wait(10)
driver.find_element_by_name("username").send_keys("batchautomation")
driver.find_element_by_name("password").send_keys("Test@12345")
driver.find_element_by_xpath("//input[@value='Login']").submit()
driver.switch_to.frame("mainpanel")
driver.find_element_by_xpath("//a[text()='Companies']").click()
companyName = "Aa Anand Testing"

# Method 1
total_rows = len(driver.find_elements_by_xpath("//form[@id='vCompaniesForm']/table//tr"))
xpath1 = "//form[@id='vCompaniesForm']/table//tr["
xpath2 = "]/td[2]/a"

for i in range(5, total_rows):
    actual_company = driver.find_element_by_xpath(xpath1 + str(i) + xpath2).text
    if companyName == actual_company:
        driver.find_element_by_xpath(xpath1 + str(i) + "]/td[1]/input").click()
        driver.get_screenshot_as_file(os.getcwd() + "\\Demo04_DynamicWebTable_Method1.png")
        break

# Method 2 - > Preferred approach in case of perfomance

driver.find_element_by_xpath("//a[contains(text(),'" + companyName
                             + "')]/parent::td/preceding-sibling::td/input[@name='client_id']").click()
driver.get_screenshot_as_file(os.getcwd() + "\\Demo04_DynamicWebTable_Method2.png")
driver.quit()
