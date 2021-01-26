class_column = 'match'

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

base_feature_names = [
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
]