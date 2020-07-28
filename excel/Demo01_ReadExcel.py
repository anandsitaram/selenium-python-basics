import xlrd
import os

workbook=xlrd.open_workbook(os.getcwd()+"\\TestData_xls.xls")

sheet=workbook.sheet_by_name("Sheet2")

rows=sheet.nrows
cols=sheet.ncols

#All rows  and colums
for row in range(0,rows):
    for col in range(0,cols):
        print(sheet.cell_value(row,col))