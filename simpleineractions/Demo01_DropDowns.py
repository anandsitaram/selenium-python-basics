from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.implicitly_wait(30)
driver.maximize_window()
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").submit()
driver.find_element_by_id("menu_recruitment_viewRecruitmentModule").click()

ele=driver.find_element_by_id("candidateSearch_status")
sel=Select(ele)
print("is it multi select- ",sel.is_multiple)
print("-----All options--------")
for a in sel.options:
    print(a.text)
print("--------------------")
print("1.Selected option is ",sel.first_selected_option.text)
sel.select_by_index(2)
print("2.Selected option is ",sel.first_selected_option.text)
sel.select_by_visible_text("Interview Failed")
print("3.Selected option is ",sel.first_selected_option.text)
sel.select_by_value("OFFER DECLINED")
print("4.Selected option is ",sel.first_selected_option.text)

#You  can deselect options of a multi-select

driver.get("https://www.jqueryscript.net/demo/Two-side-Multi-Select-Plugin-with-jQuery-multiselect-js/")
ele=driver.find_element_by_id("undo_redo")
sel=Select(ele)
print("-----All options--------")
for a in sel.options:
    print(a.text)
print("----------------------")
print("is it multi select- ",sel.is_multiple)

sel.select_by_index(5)
print("5.Selected option is ",sel.first_selected_option.text)
sel.deselect_by_index(5)
print("6.Selected option count is ",len(sel.all_selected_options))
sel.select_by_value("4")
sel.select_by_visible_text("PHP")
print("7.Selected option count is ",len(sel.all_selected_options))
print("-----All selected options--------")
for a in sel.all_selected_options:
    print(a.text)
sel.deselect_all()
print("8.Selected option count is ",len(sel.all_selected_options))

driver.quit()