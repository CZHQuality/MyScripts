import tensorflow as tf 
import numpy as np 
'''
# A = tf.random_uniform([1,4,4,3], 0, 10) 
A = tf.ones([1,4,4,3])
B = A[0,:,:,1]
# A = tf.ones([1,4,4,3]) 

with tf.Session() as sess:
    print(sess.run(A))
    print(sess.run(B))
  #  print("A is :", A)
# print("A is :", A)

max = 

# B = A[0,:,:,1]
# with tf.Session() as sess:
  #  print(sess.run(B))
'''

A1 = np.ones([4,4])
A2 = np.ones([4,4]) * 2
A3 = np.ones([4,4]) * 3

# B1 = tf.zeros([4,4,3])
B1 = np.zeros((4,4,3))
# print(B1)

B1[:,:,0] = A1
B1[:,:,1] = A2
B1[:,:,2] = A3

B1 = tf.convert_to_tensor(B1)

B2 = tf.expand_dims(B1, 0)
with tf.Session() as sess:
    print(sess.run(B1))
    print(sess.run(B2))

