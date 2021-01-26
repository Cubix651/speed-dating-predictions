class_column = 'match'

attributes = [
    'attr',
    'sinc',
    'intel',
    'fun',
    'amb',
    'shar',
]

attributes_long_names = {
    'attr':'Atrakcyjny',
    'sinc':'Szczery',
    'intel':'Inteligentny',
    'fun':'Zabawny',
    'amb':'Ambitny',
    'shar':'Wspólne zainteresowania',
}

person_preference = lambda a: a+'1_1'
person_opinion = lambda a: a
partner_preference = lambda a: 'pf_o_'+a[:3]
partner_opinion = lambda a: a+'_o'

variants_person = (
    person_preference,
    person_opinion
)
variants_partner = (
    partner_preference,
    partner_opinion
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