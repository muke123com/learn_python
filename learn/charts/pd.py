import pandas as pd
import numpy as np

df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                   "date": pd.date_range('20130102', periods=6),  # !
                   "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32],
                   "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},  # !
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])

df1 = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
                    "gender": ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
                    "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y', ],
                    "m-point": [10, 12, 20, 40, 40, 40, 30, 20]})

print(df.shape)
print(df.dtypes)
print(df.info())

print(df.isnull())
print(df.values)

df_inner = pd.merge(df, df1, how='inner')  # 匹配合并，交集
df_left = pd.merge(df, df1, how='left')  #
df_right = pd.merge(df, df1, how='right')
df_outer = pd.merge(df, df1, how='outer')  # 并集

result = df.append(df1)
# 设置索引列
df_inner.set_index('id')
# 按照特定列的值排序
df_inner.sort_values(by=['age'])
# 按照索引列排序
df_inner.sort_index()
# 如果prince列的值>3000，group列显示high，否则显示low
df_inner['group'] = np.where(df_inner['price'] > 3000, 'high', 'low')
# 对复合多个条件的数据进行分组标记
df_inner.loc[(df_inner['city'] == 'Shenzhen') & (df_inner['price'] <= 4000), 'sign'] = 1
# 对category字段的值依次进行分列，并创建数据表，索引值为df_inner的索引列，列名称为category和size
split = pd.DataFrame((x.split('-') for x in df_inner['category']), index=df_inner.index, columns=['category-s', 'size'])
df_inner = pd.merge(df_inner, split, right_index=True, left_index=True)

# 数据提取
# 主要用到的三个函数：loc,iloc和ix，loc函数按标签值进行提取，iloc按位置进行提取，ix可以同时按标签和位置进行提取。

pass
