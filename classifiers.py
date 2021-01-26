import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import tensorflow as tf

def __run(classifier, dataset):
    print(20*'=')
    name = str(classifier)
    print(name)
    classifier.fit(dataset.train_inputs, dataset.train_classes)
    class_names = classifier.classes_
    score = classifier.score(dataset.test_inputs, dataset.test_classes)
    print(score)

    predicted_classes = classifier.predict(dataset.test_inputs)
    matrix = confusion_matrix(dataset.test_classes, predicted_classes)
    mdf = pd.DataFrame(matrix, columns=class_names, index=class_names)
    print(mdf)

    return name, score

def run_decision_tree_classifier(dataset):
    __run(DecisionTreeClassifier(), dataset)

def run_naive_bayes_classifier(dataset):
    __run(GaussianNB(), dataset)

def run_k_neighbors_classifier(k, dataset):
    __run(KNeighborsClassifier(n_neighbors=k, metric='euclidean'), dataset)

def run_neural_network(dataset):
    print(20*'=')
    print('NeuralNetwork')
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(31, input_shape=(31,), activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(2, activation='softmax')
    ])
    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics=['accuracy']
    )
    model.fit(dataset.train_inputs, dataset.train_classes, epochs=30, verbose=0)
    _, accuracy = model.evaluate(dataset.test_inputs, dataset.test_classes, verbose=0)
    print(accuracy)
    predictions = model.predict(dataset.test_inputs)
    output_classes = np.argmax(predictions, axis=1)
    matrix = confusion_matrix(dataset.test_classes, output_classes)
    class_names = [0,1]
    mdf = pd.DataFrame(matrix, columns=class_names, index=class_names)
    print(mdf)