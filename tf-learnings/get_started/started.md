# Getting Started with TensorFlow
Tensorflow提供了不同层次的API，最底层的API是**Tensorflow Core**，它提供了最完整最全面的API。我们建议机器学习研究人员和那些想要完全掌握模型细节的工程师使用Tensorflow Core。为了简化Tensorflow的使用，Tensorflow还提供了接口简单的高层的API，高层API都建立在Tensorflow Core之上。建议初学者使用这些高层API学习。注意，许多高层API方法包含`contrib`，这意味着这些API还处在开发阶段，处于开发阶段的方法将来可能随时改变甚至被删掉。


我们先学习Tensorflow Core，接下来使用tf.contrib.learn实现相同的模型。只有了解Tensorflow Core才能知道高层API的内部工作方式。


## Tensors

Tensorflow中的核心概念是**tensor**。tensor，也就是张量，维度任意，元素类型相同。用**rank**表示tensor的维度：

```
3 # 常数的rank是0，shape是[]
[1. ,2., 3.] # rank是1，这是一个向量，shape是[3]
[[1., 2., 3], [4., 5., 6]] # rank是2，这是一个矩阵，shape是[2, 3]
[[[1. ,2., 3.]], [[7., 8., 9.]]] # rank是3，shape是[2, 1, 3]
# rank=前面的[个数
```



### Tensorflow Core tutorial

**Importing Tensorflow**

```
import tensorflow as tf
```
**The Computational Graph**

你可以把Tensorflow Core程序理解为两个步骤：

1. 创建computational graph

2. 执行computational graph


先来创建一个简单的计算图(computational graph)，每个节点都有>=0个tensor作为输入，和一个输出tensor。有一类节点是constant节点，这类节点不需要输入tensor，输出tensor即节点的存储值。

我们来创建两个浮点tensor:

```
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) # 默认是tf.float32
print(node1, node2)

```


输出是
```
(<tf.Tensor 'Const:0' shape=() dtype=float32>, <tf.Tensor 'Const_1:0' shape=() dtype=float32>)
```

注意print并不会输出3.0和4.0的值。相反，输出的是两个节点，只有求值(evaluate)才会产生3.0和4.0。只有在**session**内执行计算图，才能对节点求值。一个session包含了Tensorflow运行时的控制和状态。



接下来创建一个`Session`对象，然后调用`run`方法来执行计算图，对两个节点求值。

```
sess = tf.Session()
print(sess.run([node1, node2]))


```


输出是:

```
[3.0, 4.0]

```


Tensorflow中操作运算也是节点，我们来创建更复杂的计算图：

```
node3 = tf.add(node1, node2)
print("node3: ", node3)
print("sess.run(node3): ", sess.run(node3))

```

输出

```
('node3: ', <tf.Tensor 'Add:0' shape=() dtype=float32>)
('sess.run(node3): ', 7.0)
```


Tensorflow提供一个可视化模块TensorBoard，可以显示计算图。计算图也可以接受外部输入，这时需要使用**placeholdeer**。一个placeholder并不会在创建时提供初始值，而是在以后提供一个值。

```
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b # + 等同于tf.add(a, b), 是缩写




```


我们接下来对这个计算图求值，使用feed_dict参数来输入tensor值:

```
print(sess.run(adder_node, {a: 3, b: 4.5}))
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))
```
输出是
```
7.5
[3., 7.]
```

继续添加节点，

```
add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b: 4.5}))
```
输出
```
22.5
```


机器学习模型都包含必不可少的参数，一般用**Variable**表示模型的参数，

```
W = tf.Variable([3.], tf.float32)
b = tf.Variable([-.3], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b

```


constant在调用`tf.constant`创建时需要初始化，它的值永远不会改变。相反，variable在调用`tf.Variable'创建时不会执行初始化。如何初始化variable呢？你必须调用一个特殊操作：

```
init = tf.global_variables_initializer()
sess.run(init)

```















