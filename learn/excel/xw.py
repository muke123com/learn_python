import xlwings as xw
import pandas as pd
import numpy as np
import datetime as dt

wb = xw.Book(r'C:\Users\Administrator\Desktop\py1.xlsx')

sht = wb.sheets[0]  # 第一个sheet, 也可以通过名字获取

sht.clear()

data = np.random.rand(10, 5)
df = pd.DataFrame(data)
sht.range('A1').value = df

chart = sht.charts.add(500, 0)
chart.set_source_data(sht.range('A1').expand())
chart.chart_type = 'line'



# print(sht.range('A1').expand().address)

# sht.range('A3').formula = '=SUM(A1:A2)'

# df = pd.DataFrame([[111, 222], ['qqq', 'www']], index=['I', 'II'], columns=['one', 'two'])
# sht.range('A1').value = df

# sht.range('A1').value = 1
# sht.range('A2').value = 'HELLO'
# sht.range('A3').value = dt.datetime(2019, 6, 13)
#
# sht.range('B1').value = [[1], [2], [3], [4], [5]]
# sht.range('C1').value = ['A', 'B', 'C', 'D', 'E']
