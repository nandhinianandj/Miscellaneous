import tensorflow as tf
import numpy  as np
names = []
indStates =[]
size = len(names)
train_X = np.array(names[:size * 2/3])
train_y = np.array(indStates[:size * 2/3])
test_X = np.array(names[size * 2/3:])
test_y = np.array(indStates[size * 2/3:])
X = tf.placeholder(tf.float32, [None, max_sequence_length, num_input])
y = tf.placeholder(tf.float32, [None, num_classes])
weights = weight_variable([num_hidden, num_classes])
biases = bias_variable([num_classes])
rnn_cell = tf.nn.rnn_cell.BasicRNNCell(num_hidden)
out, states = tf.nn.dynamic_rnn(rnn_cell, X, dtype = tf.float32)
y_ = tf.matmul(outputs[:,-1,:], weights) + biases
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = y_, labels = y))
train_step = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(loss)

