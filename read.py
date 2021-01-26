import pandas as pd
from configuration import class_column, feature_names

def read_database(path):
    df = pd.read_csv(path, 
        encoding="ISO-8859-1",
        usecols=[class_column, *feature_names])
    
    return df