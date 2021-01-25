import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.metrics import confusion_matrix

attributes = [
    'attr',
    'sinc',
    'intel',
    'fun',
    'amb',
    'shar',
]
variants_person = (
    lambda a: a+'1_1',
    lambda a: a,
)
variants_partner = (
    lambda a: 'pf_o_'+a[:3],
    lambda a: a+'_o',
)
variants = list(variants_person) + list(variants_partner)
attributes_variants = [
    v(a) for a in attributes for v in variants
]

def all_attributes_scale_to_alloc(df):
    for variant in variants:
        current_attributes = list(map(variant, attributes))
        attributes_scale_to_alloc(df, current_attributes)

def attributes_scale_to_alloc(df, attributes):
    sum = df[attributes].sum(axis=1)
    result = df[attributes].div(sum, axis=0) * 100
    print(result)
    df.loc[:,attributes] = result

def main():
    
    base_feature_names = [
        'wave',
        'age',
        'age_o',
        'race',
        'race_o',
        'date',
        'go_out',
        'exphappy',
    ]
    feature_names = [
        *base_feature_names,
        *attributes_variants,
        # *['person_ratio_' + a for a in attributes],
        # *['partner_ratio_' + a for a in attributes],
    ]
    class_column = 'match'

    df = pd.read_csv('db/Speed Dating Data.csv', 
        encoding="ISO-8859-1",
        usecols=[class_column, *base_feature_names, *attributes_variants])
    
    df.dropna(inplace=True)

    condition = (df['wave'] >= 6) & (df['wave'] <= 9)
    # print(condition)
    rows_with_scale = df[condition]
    print(rows_with_scale)
    all_attributes_scale_to_alloc(rows_with_scale)
    print(rows_with_scale)
    
    # for attribute in attributes:
    #     for desired, real, kind in [(*variants_person, 'person'), (*variants_partner, 'partner')]:
    #         real_attribute = real(attribute)
    #         desired_attribute = desired(attribute)
    #         attribute_ratio = (df[real_attribute] - df[desired_attribute]) > 0
    #         df[kind + '_ratio_' + attribute] = attribute_ratio
    #         df.drop(columns=[real_attribute, desired_attribute], inplace=True)    
    
    # print(df)
    all_inputs = df[feature_names].values
    all_classes = df[class_column].values
    (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)

    dtc = DecisionTreeClassifier()
    dtc.fit(train_inputs, train_classes)
    class_names = dtc.classes_

    score = dtc.score(test_inputs, test_classes)
    print(score)

    predicted_classes = dtc.predict(test_inputs)
    matrix = confusion_matrix(test_classes, predicted_classes)
    mdf = pd.DataFrame(matrix, columns=class_names, index=class_names)
    print(mdf)

if __name__ == '__main__':
    main()