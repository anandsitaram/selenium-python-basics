import xlrd
import os
import xlwt

from xlutils.copy import  copy

filepath=os.getcwd() + "\\TestData_xls.xls"
workbook = xlrd.open_workbook(filepath)
write_book = copy(workbook)

sheet = workbook.sheet_by_name("Sheet2")
write_sheet=write_book.get_sheet(1)

rows = sheet.nrows
cols = sheet.ncols

# Write data to existing file
for row in range(1, rows):
    write_sheet.write(row,6,"Write "+str(row))

write_book.save(filepath)

# Write data to new file
book=xlwt.Workbook()
sheet_add=book.add_sheet("New Sheet")

for row in range(0,rows):
    for col in range(0,cols):
        sheet_add.write(row,col,sheet.cell_value(row,col))

book.save(os.getcwd() + "\\NewFile_xls.xls")



