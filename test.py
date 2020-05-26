import tensorflow as tf
import numpy as np

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(8, input_shape=(4,), bias_initializer='random_uniform', kernel_initializer='random_uniform', activation='relu'))
model.add(tf.keras.layers.Dense(1, bias_initializer='random_uniform', kernel_initializer='random_uniform', activation='sigmoid'))

# x = np.array([[12,23,32,45]])
print(model.layers[0].get_weights())

#import matplotlib.pyplot as plt
#import numpy as np
#import random

#list = [[0 for i in range(2)] for j in range(5)]
#for i in range(5):
#	list[i][0] = i
#	list[i][1] = random.randrange(1,10,1)

#sorted(list, key=lambda x : x[1])

#temp = 15 * .35
#print(str(int(temp)))