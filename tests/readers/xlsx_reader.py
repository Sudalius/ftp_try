import xlrd


def get_line_from_xls(path, row):
    work_book = xlrd.open_workbook(path)
    sheet = work_book.sheet_by_index(0)
    print(sheet.row(row))
    return sheet.row(row)


def dictionary_from_xls(path, rows_quantity, keys_column, values_column):
    work_book = xlrd.open_workbook(path)
    sheet = work_book.sheet_by_index(0)
    dic = {}
    for i in range(rows_quantity):
        cell_key = sheet.cell(i, keys_column).value
        cell_value = sheet.cell(i, values_column).value
        dic[cell_key] = cell_value
    for k in dic:
        print(k + " : " + dic[k])
    return dic
