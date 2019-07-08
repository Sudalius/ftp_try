# Reading an excel file using Python
import xlrd

# Give the location of the file
file_location = "../tests/files_store/capitals.xlsx"

# To open Workbook
work_book = xlrd.open_workbook(file_location)
sheet = work_book.sheet_by_index(0)

# For row 0 and column 0
print(sheet.col_values(0, 0))