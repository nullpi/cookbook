# -*- coding: UTF-8 -*-
from openpyxl import  Workbook

workbook = Workbook()
sheet1 = workbook.active
sheet1.cell(1, 1, '这是一个单元格')
workbook.save('新建 XLSX 工作表.xlsx')