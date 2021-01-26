import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from read import read_database
from configuration import feature_names, class_column
from classifiers import *
from dataset import DataSet

def main():
    df = read_database('db/Speed Dating Data.csv')

    df.dropna(inplace=True)
    
    # print(df)
    all_inputs = df[feature_names].values
    all_classes = df[class_column].values
    dataset = DataSet(*train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1))

    run_decision_tree_classifier(dataset)
    run_naive_bayes_classifier(dataset)
    for k in [3, 5, 7]:
        run_k_neighbors_classifier(k, dataset)
    run_neural_network(dataset)

if __name__ == '__main__':
    main()