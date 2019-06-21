import numpy as np
import operator


# numbers = np.array([1, 2, 3, 4])
# print(numbers)
# print(numbers.dtype)  # 类型统一
# print(numbers == 2)
#
# isTwo = (numbers == 2)
# print(numbers[isTwo])
#
# matrix = np.array([
#     [5, 10, 15],
#     [15, 20, 25],
#     [25, 30, 35],
# ])
#
# sc_25 = (matrix[:, 2] == 25)
# print(sc_25)
# print(matrix[sc_25, :])
#
# numbers = numbers.astype(float)
# print(numbers.dtype)
# print(numbers)
#
# print(matrix.sum())
# print(matrix.sum(axis=1))  # 对行求和
# print(matrix.sum(axis=0))  # 对列求和
# print(np.sqrt(matrix))  # 平方根

# # 矩阵
# r_arr = np.random.rand(2, 2)
# r_mat = np.mat(r_arr)   # 数组转矩阵
# print(r_mat)
# print('***********************************')
# print(r_mat.I)          # 矩阵求逆
# print('***********************************')
# print(r_mat * r_mat.I)
# print(np.eye(2))        # 创建单位矩阵

# group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0.1]])
# print(group.shape[0])
# print(np.tile([0,0], (group.shape[0], 1))-group)

