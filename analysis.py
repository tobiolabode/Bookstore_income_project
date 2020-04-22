import pandas as pd
import re
pd.set_option('display.max_colwidth', -1)

Postcodes = ['EN', 'IG', 'RM', 'DA', 'BR', 'TN', 'CR', 'SM', 'KT',
             'TW', 'HA', 'UB', 'E', 'EC', 'N', 'NW', 'SE', 'SW', 'W', 'WC']

Postcode_regex = '([A-Z]{1,2}[0-9][0-9A-Z]? [0-9][A-Z]{2})'
# https://regexr.com/52ni1

London_postcode_regex = '([^A-Z]E[0-9]|EC[0-9]|[^A-Z]N[0-9]|NW[0-9]|SE[0-9]|SW[0-9]|[^A-Z]W[0-9]|WC[0-9]|[E]N[0-9]|[I]G[0-9]|[R]M[0-9]|[D]A[0-9]|[B]R[0-9]|[T]N[0-9]|[C]R[0-9]|[S]M[0-9]|[K]T[0-9]|[T]W[0-9]|[H]A[0-9]|[U]B[0-9])'

dataset_df = pd.read_csv('dataset.csv')
dataset_df['Postcode'] = dataset_df[' Street_name'].str.extract(Postcode_regex)
dataset_df = dataset_df.drop('Town', axis=1)
filtered_column = dataset_df.Postcode.str.contains(London_postcode_regex)
# print(filtered_column)
dataset_df = dataset_df[dataset_df['Postcode'].str.contains(London_postcode_regex) == True]

print(dataset_df.head(10))

# print(dataset_df.dtypes)
