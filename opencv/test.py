import cv2 as cv
import tensorflow as tf

a = tf.constant(3)
b = tf.constant(7)
c = tf.multiply(a,b)
sess = tf.Session()
_c = sess.run(c)
print(_c)