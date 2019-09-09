from openpyxl import Workbook
from openpyxl.chart import BarChart, Series, Reference

wb = Workbook()
ws = wb.active

rows = [
    ('月份', '产品A', '产品B'),
    (2, 10, 30),
    (3, 40, 60),
    (4, 50, 70),
    (5, 20, 10),
    (6, 10, 40),
    (7, 50, 30),
]

for row in rows:
    ws.append(row)

chart1 = BarChart()
chart1.type = "col"


chart1.title = "AB产品销量对比"
chart1.y_axis.title = '销售额（万元）'
chart1.x_axis.title = '月份'

data = Reference(ws, min_col=2, min_row=1, max_row=7, max_col=3)
cats = Reference(ws, min_col=1, min_row=2, max_row=7)
chart1.add_data(data, titles_from_data=True)
chart1.set_categories(cats)

ws.add_chart(chart1, "B10")

wb.save("bar.xlsx")