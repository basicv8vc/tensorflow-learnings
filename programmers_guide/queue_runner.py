#-*- coding:utf-8 -*-

import tensorflow as tf

example = ...ops to create one example...

# Create a queue和一个入队op，每次把一个example入队
queue = tf.RandomShuffleQueue(...)
enqueue_op = queue.enqueue(example)
# Create a training graph
inputs = queue.dequeue_many(batch_size)
train_op = ...use 'inputs' to build the training part of the graph...

# Create a queue runner that will run 4 threads in parallel
qr = tf.train.QueueRunner(queue, [enqueue_op] * 4)

sess = tf.Session()

# Create a coordinator, 
coord = tf.train.Coordinator()
enqueue_threads = qr.create_threads(sess, coord=coord, start=True)

# 
try:
    for step in xrange(100000):
        if coord.should_stop():
            break
        sess.run(train_op)
except Exception e:
    # Report exceptions to the coordinator
    coord.request_stop(e)
finally:
    # Terminate as usuall. 调用coord.request_stop()多次是安全的
    coord.request_stop()
    coord.join(enqueue_threads)

