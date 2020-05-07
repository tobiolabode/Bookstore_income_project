import pandas as pd
import re
import matplotlib.pyplot as plt
pd.set_option('display.max_colwidth', -1)
# pd.set_option('display.max_columns', None)

Postcodes = ['EN', 'IG', 'RM', 'DA', 'BR', 'TN', 'CR', 'SM', 'KT',
             'TW', 'HA', 'UB', 'E', 'EC', 'N', 'NW', 'SE', 'SW', 'W', 'WC']

Postcode_regex = '([A-Z]{1,2}[0-9][0-9A-Z]? [0-9][A-Z]{2})'
# https://regexr.com/52ni1

London_postcode_regex = '([^A-Z]E[0-9]|EC[0-9]|[^A-Z]N[0-9]|NW[0-9]|SE[0-9]|SW[0-9]|[^A-Z]W[0-9]|WC[0-9]|[E]N[0-9]|[I]G[0-9]|[R]M[0-9]|[D]A[0-9]|[B]R[0-9]|[T]N[0-9]|[C]R[0-9]|[S]M[0-9]|[K]T[0-9]|[T]W[0-9]|[H]A[0-9]|[U]B[0-9])'
Greater_london_postcode_regex = '([E]N[0-9]|[I]G[0-9]|[R]M[0-9]|[D]A[0-9]|[B]R[0-9]|[T]N[0-9]|[C]R[0-9]|[S]M[0-9]|[K]T[0-9]|[T]W[0-9]|[H]A[0-9]|[U]B[0-9])'
London_bookstore_name_regex = '(London -)'

dataset_df = pd.read_csv('dataset.csv')
dataset_df['Postcode'] = dataset_df[' Street_name'].str.extract(Postcode_regex)
dataset_df = dataset_df.drop('Town', axis=1)
filtered_greater_london = dataset_df.Postcode.str.contains(Greater_london_postcode_regex)
filtered_inner_london = dataset_df['Bookstore name'].str.contains(London_bookstore_name_regex)

non_bool_filtered_greater_london = dataset_df[
    dataset_df.Postcode.str.contains(Greater_london_postcode_regex) == True]
non_bool_filtered_inner_london = dataset_df[dataset_df['Bookstore name'].str.contains(
    London_bookstore_name_regex) == True]


# print(non_bool_filtered_greater_london.head(10))
# print(non_bool_filtered_inner_london.head(10))

dataset_df['Greater_london'] = filtered_greater_london
dataset_df['Inner_london'] = filtered_inner_london
# dataset_df = dataset_df.drop(' Street_name', axis=1)

frames = [non_bool_filtered_greater_london, non_bool_filtered_inner_london]

result = pd.concat(frames)
# result = result.drop(' Street_name', axis=1)

# print(result)
#
# result.to_csv('filtered_dataset.csv', index=False)

excel_df = pd.read_excel('income-of-tax-payers.xls', sheet_name=1)

# print(excel_df.head(10))
# for col in excel_df.columns:
#     print(col)


tax_year = excel_df[['Unnamed: 1', '2016-17', 'Unnamed: 51', 'Unnamed: 52']]
tax_year = tax_year.dropna()
tax_year = tax_year.drop(tax_year.index[34:])
new_header = tax_year.iloc[0]
tax_year = tax_year[1:]
tax_year.columns = new_header
# print(tax_year)

# for col in tax_year.columns:
#     print(col)

tax_year_without_pop = tax_year.drop('Number of Individuals', axis=1)
print(tax_year_without_pop)

tax_year_without_pop.plot(kind='bar', x='Area', y='Mean £')
# plt.show()


# Linear regession question: num of Bookstores to income.

bookstore_df = pd.read_csv('filtered_dataset_boroughs.csv')
count = bookstore_df['Borough'].value_counts()
print(count)

count.to_csv('count_borough.csv')
