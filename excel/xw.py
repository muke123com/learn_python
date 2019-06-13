import xlwings as xw
import pandas as pd
import datetime as dt

wb = xw.Book(r'C:\Users\Administrator\Desktop\py1.xlsx')

sht = wb.sheets[0]

sht.range('A3').formula = '=SUM(A1:A2)'

# df = pd.DataFrame([[111, 222], ['qqq', 'www']], index=['I', 'II'], columns=['one', 'two'])
# sht.range('A1').value = df

# sht.range('A1').value = 1
# sht.range('A2').value = 'HELLO'
# sht.range('A3').value = dt.datetime(2019, 6, 13)
#
# sht.range('B1').value = [[1], [2], [3], [4], [5]]
# sht.range('C1').value = ['A', 'B', 'C', 'D', 'E']

