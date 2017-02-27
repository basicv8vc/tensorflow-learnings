#-*- coding:utf-8 -*-
import tensorflow as tf
import numpy as np

W = tf.Variable([.3], tf.float32)
b = tf.Variable([.1], tf.float32)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# 定义模型 
linear_model = W * x + b
# 定义损失函数
loss = tf.reduce_sum(tf.square(linear_model - y))

# 定义学习算法
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# 初始化Variable
init = tf.global_variables_initializer()

# 创建Session
sess = tf.Session()
sess.run(init)

# 数据集
x_train = np.array([0,1,2,3])
y_train = np.array([1,2,3,4])

for i in range(1000):
  sess.run(train, {x:x_train, y:y_train})

print(sess.run([W, b]))

