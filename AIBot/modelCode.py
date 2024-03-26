# Library Imports
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Loads dataset
data = keras.datasets.fashion_mnist

# Split dataset into training and testing sets
(tr_i, tr_l), (te_i, te_l) = data.load_data()

# Define class names for the labls
class_names = ['T-shirt', 'Trouser', 'pullover', 'dress', 'coat', 'chankle', 'sjort', 'jordans', 'bag', 'ankvootd']

# Normalize pixel values to be between 0 and 1
tr_i = tr_i/255.0
te_i = te_i/255.0

# Create the neural network model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers,Dense(10, activations="softmax")
    ])

# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(tr_i, tr_l, epochs=10)

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(te_i, tr_l)

# Print test accuracy 
print(test_acc)
