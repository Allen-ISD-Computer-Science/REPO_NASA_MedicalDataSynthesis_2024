import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist

(tr_i, tr_l), (te_i, te_l) = data.load_data()

class_names = ['T-shirt', 'Trouser', 'pullover', 'dress', 'coat', 'chankle', 'sjort', 'jordans', 'bag', 'ankvootd']

tr_i = tr_i/255.0
te_i = te_i/255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers,Dense(10, activations="softmax")
    ])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(tr_i, tr_l, epochs=10)
test_loss, test_acc = model.evaluate(te_i, tr_l)

print(test_acc)
