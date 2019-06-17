import xlwings as xw
import pandas as pd
import numpy as np
import datetime as dt

wb = xw.Book(r'C:\Users\Administrator\Desktop\py1.xlsx')

sht = wb.sheets[0]  # 第一个sheet, 也可以通过名字获取

sht.clear()

data = np.random.rand(10, 5)
data_max = np.amax(data)
data_max_index = np.unravel_index(data.argmax(), data.shape)

print(data_max)
print(data_max_index)
# 生成字母数组
chars = []
for i in range(26):
    chars.append(chr(97 + i))


def get_point():
    x = chars[data_max_index[1] + 1]
    y = data_max_index[0] + 2
    return x + str(y)


point = get_point()
print(point)

df = pd.DataFrame(data)
sht.range('A1').value = df

# print(sht.range('A1').api.Font.Color)
# print(sht.range('A1').expand('table').value)
# print(sht.range(data_max_index).value)

sht.range(point).api.Font.Size = 15
sht.range(point).api.Font.Bold = True
sht.range(point).api.Font.Color = 0x0000ff

chart = sht.charts.add(400, 0)
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
