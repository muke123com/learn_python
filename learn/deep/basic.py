import tensorflow as tf
# 创建一个常量op
m1 = tf.constant([[3, 3]])
# 创建一个常量op
m2 = tf.constant([[2], [3]])
# 创建矩阵乘法op
product = tf.matmul(m1, m2)

# 定义会话
sess = tf.compat.v1.Session()

result = sess.run(product)

print(result)
sess.close()

