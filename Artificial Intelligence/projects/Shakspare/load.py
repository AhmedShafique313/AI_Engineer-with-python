import random
import numpy as np
import tensorflow as tf

file_path = tf.keras.utils.get_file(r'shakspare.txt', r'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(file_path, 'rb').read().decode(encoding='utf-8')
