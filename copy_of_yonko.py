# -*- coding: utf-8 -*-
"""Copy of Yonko.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1czdByGbYTWCK9yv5Xhl88k32JGteSZ2a

# Difference Epochs Testing (KIV)

Adam : MSE VS MAE : Epo=1000

Discussion:
MAE showing high digit with realistic loss magnitude, so next coding will using MAE
"""

#Pridicting X=250 using Adam optimizer, Mean Square Error, Epochs = 1000

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_squared_error',
 optimizer=tf.keras.optimizers.Adam(1))
# Train the model
history = model.fit(x, y, epochs=1000, verbose=False)
Expect = history.history ['loss']
print (history.history ['loss'])
print('Loss Magnitude when epochs is 1000:', Expect [999])
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

#Pridicting X=250 using Adam optimizer, Mean Absolute Error, Epochs = 1000

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_absolute_error',
 optimizer=tf.keras.optimizers.Adam(1))
# Train the model
history = model.fit(x, y, epochs=1000, verbose=False)
Expect = history.history ['loss']
print (history.history ['loss'])
print('Loss Magnitude when epochs is 1000:', Expect [999])
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

"""Different between Epochs (With loss magnitude)


*   Higher epoch not nessesaryly giving higher value
*   500>200>1000
*   No correlation can be made
*   Need further study on what (Expect[]) mean




"""

#Pridicting X=250 using Adam optimizer, Mean Absolute Error, Epochs = 200

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_absolute_error',
 optimizer=tf.keras.optimizers.Adam(1))
# Train the model
history = model.fit(x, y, epochs=200, verbose=False)
Expect = history.history ['loss']
print (history.history ['loss'])
print('Loss Magnitude when epochs is 100:', Expect [99])
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

#Pridicting X=250 using Adam optimizer, Mean Absolute Error, Epochs = 500

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_absolute_error',
 optimizer=tf.keras.optimizers.Adam(1))
# Train the model
history = model.fit(x, y, epochs=500, verbose=False)
Expect = history.history ['loss']
print (history.history ['loss'])
print('Loss Magnitude when epcohs is 500:', Expect [499])
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

#Pridicting X=250 using Adam optimizer, Mean Absolute Error, Epochs = 1000

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_absolute_error',
 optimizer=tf.keras.optimizers.Adam(1))
# Train the model
history = model.fit(x, y, epochs=1000, verbose=False)
Expect = history.history ['loss']
print (history.history ['loss'])
print('Loss Magnitude when epcohs is 1000:', Expect [999])
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

"""Coding without loss magnitude


*   higher epoch giving lower prediction value 
*   List item


"""

#Pridicting X=250 using Adam optimizer but with Mean Absolute Error Epoch:1000

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_absolute_error',
 optimizer=tf.keras.optimizers.Adam(1))
# Train the model
history = model.fit(x, y, epochs=1000, verbose=False)
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

#Pridicting X=250 using Adam optimizer but with Mean Absolute Error Epoch 100

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_absolute_error',
 optimizer=tf.keras.optimizers.Adam(1))
# Train the model
history = model.fit(x, y, epochs=100, verbose=False)
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

"""# Mean Square Error Vs Mean Absolute Error

*   MSE resulting higher value, but with lower bias 
*   MAE resulting lower value(Prediction), with higher bias
*   Weight almost the same with +/- 0.1



*   UPDATE: weight sama, MSE bias higher
*   UPDATE: MSE & MAE could have same weight and bias
*   UPDATE: MSE always higher pridiction value
*
"""

#Pridicting X=250 using Adam optimizer but with Mean Square Error

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_squared_error',
 optimizer=tf.keras.optimizers.Adam(1))
# Train the model
history = model.fit(x, y, epochs=100, verbose=False)
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

#Pridicting X=250 using Adam optimizer but with Mean Absolute Error

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_absolute_error',
 optimizer=tf.keras.optimizers.Adam(1))
# Train the model
history = model.fit(x, y, epochs=100, verbose=False)
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

"""# Difference Optimizer Testing

---


*   Value change everytime refreshed
*   Something wrong Adadelta out of range (compare to other 7++)
*   SGD required optimizer=tf.keras.optimizers.SGD(momentum=0.9) *define momentum, usually 0.9
*   Somehow bigger value doesnt mean more accurate
"""

#using optimizer: Adagrad

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_squared_error',
 optimizer=tf.keras.optimizers.Adagrad(1))
# Train the model
history = model.fit(x, y, epochs=100, verbose=False)
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

#using optimizer: Adam

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_squared_error',
 optimizer=tf.keras.optimizers.Adam(1))
# Train the model
history = model.fit(x, y, epochs=100, verbose=False)
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

#using optimizer: SGD + momentum

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_squared_error',
 optimizer=tf.keras.optimizers.SGD(momentum=0.9))    
# Train the model
history = model.fit(x, y, epochs=100, verbose=False)
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

#using optimizer: RMSprop

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_squared_error',
 optimizer=tf.keras.optimizers.RMSprop(1))
# Train the model
history = model.fit(x, y, epochs=100, verbose=False)
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))

#using optimizer: Adadelta

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# Define layer
layer0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer0])
# Compile model
model.compile(loss='mean_squared_error',
 optimizer=tf.keras.optimizers.Adadelta(1))
# Train the model
history = model.fit(x, y, epochs=100, verbose=False)
# Prediction
print('Prediction: {}'.format(model.predict([250])))
# Get weight and bias
weights = layer0.get_weights()
print('weight: {} bias: {}'.format(weights[0], weights[1]))