import configuration as cfg
import pandas as pd

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