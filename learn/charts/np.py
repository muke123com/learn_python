import numpy as np
import xlwings as xw

a1 = np.arange(24)
a2 = a1.reshape(4, 6)

a3 = np.zeros(5, dtype=int)
a4 = np.logspace(1.0, 2.0, num=10, base=10)

a5 = a1[2: 18: 3]  # 切片

s = a5
print(s)

wb = xw.Book(r'C:\Users\Administrator\Desktop\py1.xlsx')
sht = wb.sheets[0]  # 第一个sheet, 也可以通过名字获取
sht.clear()
sht.range('A1').value = s

