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
    info.to_csv('results/database_description.csv')

def __plot_pie_with_step(values, title, step):
    bins=range(0, 11*step, step)
    __plot_pie_with_bins(values, title, bins)

def __plot_pie_with_bins(values, title, bins):
    labels = [f'{a}-{b}' for a, b in zip(bins[:-1], bins[1:])]
    __plot_pie_advanced(values, title, bins, labels)

def __plot_pie_classes(values, title, classes, labels=None):
    if labels == None:
        labels = classes
    bins = [*classes, classes[-1]+1]
    __plot_pie_advanced(values, title, bins, labels)

def __plot_pie_with_labels(values, title, labels):
    classes = range(1, len(labels)+1)
    __plot_pie_classes(values, title, classes, labels)

def __plot_pie_advanced(values, title, bins, labels):
    plt.figure()
    hist, edges = np.histogram(values, bins=bins)
    plt.pie(hist)
    plt.title(title)
    plt.legend(labels=labels)
    plt.savefig(f'results/{title}.png')
    plt.close()

def __plot_attributes(df):
    for attribute in cfg.attributes:
        attribute_name = cfg.attributes_long_names[attribute]
        __plot_pie_with_step(
            df[cfg.person_preference(attribute)].values,
            'Preferencja osoby - ' + attribute_name,
            10)
        __plot_pie_classes(
            df[cfg.person_opinion(attribute)].values,
            'Opinia osoby o partnerze - ' + attribute_name,
            range(11))
        __plot_pie_with_step(
            df[cfg.person_preference(attribute)].values,
            'Preferencja partnera - ' + attribute_name,
            10)
        __plot_pie_classes(
            df[cfg.person_opinion(attribute)].values,
            'Opinia partnera o osobie - ' + attribute_name,
            range(11))

def plot_features(df):
    __plot_attributes(df)
    __plot_pie_with_bins(df['age'].values, 'Wiek', [18, 20, 22, 24, 26, 28, 30, 35, 40, 55])
    __plot_pie_with_labels(df['race'].values, 'Rasa', cfg.race_labels)
    __plot_pie_with_labels(df['date'].values, 'Częstość randkowania', cfg.frequency_labels)
    __plot_pie_with_labels(df['go_out'].values, 'Częstość wychodzenia (niekoniecznie na randki)', cfg.frequency_labels)
    __plot_pie_classes(df['exphappy'].values, 'Ogólne szczęście', range(11))
    