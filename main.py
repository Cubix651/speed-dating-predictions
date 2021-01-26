import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import tensorflow as tf
from read import *

def main():
    df = read_database('db/Speed Dating Data.csv')

    df.dropna(inplace=True)
    
    # print(df)
    all_inputs = df[feature_names].values
    all_classes = df[class_column].values
    (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)

    def run(classifier):
        print(20*'=')
        name = str(classifier)
        print(name)
        classifier.fit(train_inputs, train_classes)
        class_names = classifier.classes_
        score = classifier.score(test_inputs, test_classes)
        print(score)

        predicted_classes = classifier.predict(test_inputs)
        matrix = confusion_matrix(test_classes, predicted_classes)
        mdf = pd.DataFrame(matrix, columns=class_names, index=class_names)
        print(mdf)

        return name, score

    def run_neural_network():
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
        model.fit(train_inputs, train_classes, epochs=30, verbose=0)
        _, accuracy = model.evaluate(test_inputs, test_classes, verbose=0)
        print(accuracy)
        predictions = model.predict(test_inputs)
        output_classes = np.argmax(predictions, axis=1)
        matrix = confusion_matrix(test_classes, output_classes)
        class_names = [0,1]
        mdf = pd.DataFrame(matrix, columns=class_names, index=class_names)
        print(mdf)

    run(DecisionTreeClassifier())
    run(GaussianNB())
    for k in [3, 5, 7]:
        run(KNeighborsClassifier(n_neighbors=k, metric='euclidean'))
    run_neural_network()



if __name__ == '__main__':
    main()