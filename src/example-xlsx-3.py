from openpyxl import  Workbook

workbook = Workbook()

worksheet = workbook.active
workbook.remove(worksheet)

for m in range(1, 13):
    title = str(m) + "月份"
    workbook.create_sheet(title)

workbook.save('12张工作表.xlsx')