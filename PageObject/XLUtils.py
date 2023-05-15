import openpyexcel


def GetRow(file, sheetname):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook.get_sheet_by_name(sheetname)
    return sheet.max_row


def ReadData(file, sheetname, rownum, colomnnum):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook.get_sheet_by_name(sheetname)
    return sheet.cell(row=rownum, column=colomnnum).value
