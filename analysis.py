import pandas as pd
import re
pd.set_option('display.max_colwidth', -1)

Postcodes = ['EN', 'IG', 'RM', 'DA', 'BR', 'TN', 'CR', 'SM', 'KT',
             'TW', 'HA', 'UB', 'E', 'EC', 'N', 'NW', 'SE', 'SW', 'W', 'WC']

Postcode_regex = '([A-Z]{1,2}[0-9][0-9A-Z]? [0-9][A-Z]{2})'
# https://regexr.com/52ni1

dataset_df = pd.read_csv('dataset.csv')
dataset_df['Postcode'] = dataset_df[' Street_name'].str.extract(Postcode_regex)
dataset_df = dataset_df.drop('Town', axis=1)
filtered_dataset_df = dataset_df[dataset_df.isin(Postcodes)]
print(filtered_dataset_df.head(10))
# print(dataset_df.head(10))

# print(dataset_df.dtypes)
