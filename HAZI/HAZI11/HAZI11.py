import tensorflow as tf
import numpy as np


def cifar100_data():
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar100.load_data()

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    return train_images, train_labels, test_images, test_labels

def cifar100_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(32, 32)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(100, activation='softmax')
    ])
    return model

def model_compile(model: tf.keras.Sequential):
    model.compile(
        optimizer="adam",
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        metrics=['accuracy']
    )
    return model

def model_fit(model: tf.keras.Sequential, epochs, train_images, train_labelsz):
    model.fit(train_images, train_labelsz, epochs=epochs)
    return model

def model_evaluate(model: tf.keras.Sequential, test_images, test_labels):
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    return test_loss, test_acc
