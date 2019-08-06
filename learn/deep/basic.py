import tensorflow as tf

sess = tf.compat.v1.Session()
t1 = tf.constant(10)
t1_r = sess.run(t1)
print(t1_r)

t2 = tf.constant([[2, 2], [2, 2]])
t2_r = sess.run(t2)
print(t2_r)

t3 = tf.Variable(0, name="counter")
t3_one = tf.constant(1)
t3_new_value = tf.add(t3, t3_one)
t3_update = tf.compat.v1.assign(t3, t3_new_value)

t3_init_op = tf.compat.v1.global_variables_initializer()
sess.run(t3_init_op)
print(sess.run(t3))

for _ in range(3):
    sess.run(t3_update)
    print(sess.run(t3))



sess.close()