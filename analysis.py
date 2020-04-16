import pandas as pd
pd.set_option('display.max_colwidth', -1)

Postcodes = ['EN', 'IG', 'RM', 'DA', 'BR', 'TN', 'CR', 'SM', 'KT',
             'TW', 'HA', 'UB', 'E', 'EC', 'N', 'NW', 'SE', 'SW', 'W', 'WC']

dataset_df = pd.read_csv('dataset_no_quotes.csv')
print(dataset_df.head(10))

# print(dataset_df.dtypes)
