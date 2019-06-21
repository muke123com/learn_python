import pandas as pd
import numpy as np
import xlwings as xw
import matplotlib.pyplot as plt

nba_final_win_data = pd.read_csv(r'./championsdata.csv')
nba_final_lose_data = pd.read_csv(r'./runnerupsdata.csv')

# 根据索引算出某列数据平均值
# 每个队的总决赛平均得分
team_win_points = nba_final_win_data.pivot_table(index='Year', values='PTS', aggfunc=np.mean)
team_lose_points = nba_final_lose_data.pivot_table(index='Year', values='PTS', aggfunc=np.mean)
# print(team_win_points)
# print(team_lose_points)

# print(series_pts.values)
#
fig = plt.figure()
plt.plot(team_win_points)
plt.plot(team_lose_points)
plt.xlabel('Year')
plt.ylabel('PTS')
plt.xticks(rotation=45)
plt.show()

# 生成图片添加到excel中
wb = xw.Book(r'C:\Users\Administrator\Desktop\py1.xlsx')
sht = wb.sheets[0]  # 第一个sheet, 也可以通过名字获取
sht.clear()
sht.pictures.add(fig, name='MyPlot', update=True)