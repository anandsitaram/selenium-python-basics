import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def wait_for_pageLoad(driver):
    flag = driver.execute_script("return document.readyState;") == 'complete'
    print(driver.execute_script("return document.readyState;"))
    count = 5;
    while count!=0 and flag==False:
        time.sleep(5)
        count -= 1


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://news.google.co.in/")
driver.maximize_window()

# Example to find out Web page screen height
actual_width = driver.execute_script("return document.body.scrollHeight;");

# Scroll down till last
driver.execute_script("window.scroll(0," + str(actual_width) + ")")

# Wait for 5s
driver.execute_async_script("window.setTimeout(arguments[arguments.length-1],5000)")

# Scroll up till first
driver.execute_script("window.scroll(0,-" + str(actual_width) + ")")

driver.get("https://opensource-demo.orangehrmlive.com/")

username = driver.find_element_by_id("txtUsername")
password = driver.find_element_by_id("txtPassword")
click = driver.find_element_by_id("btnLogin")

# Entering the text
driver.execute_script("arguments[0].value='Admin';", username)
driver.execute_script("arguments[0].value='admin123';", password)
# clicking
driver.execute_script("arguments[0].click();", click)

# Wait for a time
wait_for_pageLoad(driver)
print(driver.title)

driver.quit()
