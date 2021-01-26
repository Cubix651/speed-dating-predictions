import configuration as cfg
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def describe_database(df):
    features = df[cfg.feature_names]
    info = pd.concat([
        features.min(),
        features.max(),
        features.mean(),
        features.isnull().sum() / len(features)
    ], axis=1)
    info.columns = ['min', 'max', 'mean', 'isnull']
    print(info)
    info.to_csv('database_description.csv')

def __plot_pie(values, step, title):
    plt.figure()
    hist, edges = np.histogram(values, bins=range(0, 10*step + 1, step))
    labels = [f'{a}-{b}' for a, b in zip(edges[:-1], edges[1:])]
    plt.pie(hist, labels=labels)
    plt.title(title)
    plt.savefig(f'results/{title}.png')
    plt.close()

def __plot_attributes(df):
    for attribute in cfg.attributes:
        attribute_name = cfg.attributes_long_names[attribute]
        __plot_pie(
            df[cfg.person_preference(attribute)].values,
            10,
            'Preferencja osoby - ' + attribute_name)
        __plot_pie(
            df[cfg.person_opinion(attribute)].values,
            1,
            'Opinia osoby o partnerze - ' + attribute_name)
        __plot_pie(
            df[cfg.person_preference(attribute)].values,
            10,
            'Preferencja partnera - ' + attribute_name)
        __plot_pie(
            df[cfg.person_opinion(attribute)].values,
            1,
            'Opinia partnera o osobie - ' + attribute_name)

def plot_features(df):
    __plot_attributes(df)
    