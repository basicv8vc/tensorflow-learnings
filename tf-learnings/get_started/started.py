#-*- coding:utf-8 -*-
import tensorflow as tf

#node1 = tf.constant(3.0, tf.float32)
#node2 = tf.constant(4.0)

#print(node1, node2)

sess = tf.Session()
#print(sess.run([node1, node2]))

#node3 = tf.add(node1, node2)    
#print("node3: ", node3)
#print("sess.run(node3): ", sess.run(node3))


a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b # + 等同于tf.add(a, b), 是缩写


#print(sess.run(adder_node, {a: 3, b: 4.5}))
#print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))


add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b: 4.5}))