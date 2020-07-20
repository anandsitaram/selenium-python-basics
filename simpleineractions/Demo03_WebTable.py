from builtins import object

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_rows_cols(rows_column_rows):
    for row in rows_column_rows:
        cols = row.find_elements_by_tag_name("td")
        for col in cols:
            print(col.text)


def get_allColumn_text(rows_column_text, header):
    index = get_header(rows_column_text, header)
    for r in rows_column_text:
        cols = r.find_elements_by_tag_name("td")
        if len(cols) > 0:
            print(cols[index].text)


def get_header(rows_header, header):
    index = 0
    headers = rows_header[0].find_elements_by_tag_name("th")
    for i in range(len(headers)):
        if headers[i].text == header:
            index = i
            break
    return index


def get_cell_text(row_cell_text, row_index, col_index):
    cols = row_cell_text[row_index].find_elements_by_tag_name("td")
    print(cols[col_index].text)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.seleniumeasy.com/test/table-sort-search-demo.html")
driver.implicitly_wait(10)
driver.maximize_window()

table = driver.find_element_by_id("example")
rows = table.find_elements_by_tag_name("tr");

print("---All rows and columns text ---------")
get_rows_cols(rows)
print("--------------------")
get_allColumn_text(rows, "Salary")
print("-------------------")
get_cell_text(rows, 5, 3)

driver.quit()
