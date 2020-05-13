import pdb
import pandas as pd
import re
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
from scipy import stats
import numpy as np
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
# print(tax_year_without_pop)

# tax_year_without_pop.plot(kind='bar', x='Area', y='Mean £')
# # plt.show()


# Linear regession question: num of Bookstores to income.

bookstore_df = pd.read_csv('filtered_dataset_boroughs.csv')
count = bookstore_df['Borough'].value_counts().rename_axis('Borough').reset_index(name='Count')


count['Borough'] = count['Borough'].str.replace('London Borough of ', '')
count['Borough'] = count['Borough'].str.replace('Royal Borough of ', '')
count['Borough'] = count['Borough'].str.replace('City of Westminster', 'Westminster', regex=True)
count['Borough'] = count['Borough'].str.replace('Corporation', '').str.strip()


compare_1 = tax_year_without_pop['Area'].reset_index(drop=True)
compare_2 = count['Borough']
compare_1 = compare_1.sort_values()
compare_2 = compare_2.sort_values().reset_index(drop=True)
# print(compare_1)
# print(compare_2)

idx1 = pd.Index(compare_1)
idx2 = pd.Index(compare_2)
# print(idx1.difference(idx2).values)
append_values = idx1.difference(idx2).values
zero_list = [0] * len(append_values)

# print(append_values)
# print(zero_list)

extra_name_df = pd.DataFrame(list(zip(append_values, zero_list)), columns=['Borough', 'Count'])

# print(extra_name_df)
extra_name_df = extra_name_df.drop([5, 8])
print(extra_name_df)

count = count.append(extra_name_df, ignore_index=True)


# print(count)
count.to_csv('count_borough.csv', index=False)

count_df = pd.read_csv('count_borough.csv')
count_df = count_df.sort_values('Borough')
count_df = count_df.reset_index(drop=True)
tax_year_without_pop = tax_year_without_pop.sort_values('Area')
# print(count_df)
# print(tax_year_without_pop)

tax_year_without_pop = tax_year_without_pop.drop('Median £', axis=1)
tax_year_without_pop = tax_year_without_pop.reset_index(drop=True)
print(tax_year_without_pop)


mean_income = tax_year_without_pop['Mean £']
mean_income = mean_income.reset_index(drop=True)
# print(mean_income)
# count_df = count_df.sort_values(by='Borough')
count_df = count_df.reset_index(drop=True)
count_df['Income'] = mean_income
# print(count_df['Income'])
print(count_df)

North_names = '(Barnet|Enfield|Haringey)'
South_names = '(Bromley|Croydon|Kingston upon Thames|Merton|Sutton|Wandsworth)'
East_names = '(Barking and Dagenham|Bexley|Greenwich|Hackney|Havering|Lewisham|Newham|Redbridge|Tower Hamlets|Waltham Forest)'
West_names = '(Brent|Ealing|Hammersmith and Fulham|Harrow|Richmond upon Thames|Hillingdon|Hounslow)'
Central_names = '(Camden|City of London|Kensington and Chelsea|Islington|Lambeth|Southwark|Westminster)'

count_df['Compass'] = [0] * len(count_df['Borough'])

count_df['Compass'] = count_df['Compass'].mask((count_df['Borough'].str.contains(
    North_names) == True), other='North')

count_df['Compass'] = count_df['Compass'].mask((count_df['Borough'].str.contains(
    South_names) == True), other='South')

count_df['Compass'] = count_df['Compass'].mask((count_df['Borough'].str.contains(
    East_names) == True), other='East')

count_df['Compass'] = count_df['Compass'].mask((count_df['Borough'].str.contains(
    West_names) == True), other='West')

count_df['Compass'] = count_df['Compass'].mask((count_df['Borough'].str.contains(
    Central_names) == True), other='Central')

print(count_df)


count_df.to_csv('Borough_income_count.csv', index=False)

compass_df = pd.read_csv('Borough_income_count.csv')
print(compass_df)
groups = compass_df.groupby('Compass')
fig = plt.figure()
ax = fig.add_subplot(111)
# ax.set_xlim(-.4, .4)
for name, group in groups:
    ax.plot(group["Count"], group["Income"], marker="o", linestyle="", label=name)

# for i, txt in enumerate(compass_df['Borough']):
#     ax.annotate(txt, (compass_df['Count'].iloc[i], compass_df['Income'].iloc[i]))
#     print(i)
    # ax.annotate('test', xy=(4, 3))

ax.annotate(compass_df['Borough'].iloc[5],
            (compass_df['Count'].iloc[5], compass_df['Income'].iloc[5]))

ax.annotate(compass_df['Borough'].iloc[6],
            (compass_df['Count'].iloc[6], compass_df['Income'].iloc[6]))

ax.annotate(compass_df['Borough'].iloc[32],
            (compass_df['Count'].iloc[32], compass_df['Income'].iloc[32]))  # Westminster

ax.annotate(compass_df['Borough'].iloc[19],
            (compass_df['Count'].iloc[19], compass_df['Income'].iloc[19]))


# ax1 = count_df_no_outliers.plot.scatter(x='Count', y='Income')
# ax1 = ax1.set_ylim(bottom=0)
# # ax2 = count_df.plot.bar(x='Count', y='Income')
#
# x = compass_df['Count'].astype('float')
# y = compass_df['Income'].astype('float')
#
# b, m = polyfit(x, y, 1)
# plt.plot(x, y, '.')
# plt.plot(x, b + m * x, '-')

ax.legend()

count_df_no_outliers = count_df

count_df_no_outliers['Income'] = count_df_no_outliers['Income'][count_df_no_outliers['Income'].between(
    count_df_no_outliers['Income'].quantile(.15), count_df_no_outliers['Income'].quantile(.85))]

count_df_no_outliers = count_df_no_outliers.dropna()
# print(count_df_no_outliers)

# ax1 = count_df_no_outliers.plot.scatter(x='Count', y='Income')
# ax1 = ax1.set_ylim(bottom=0)
# # ax2 = count_df.plot.bar(x='Count', y='Income')
#
# x = count_df_no_outliers['Count'].astype('float')
# y = count_df_no_outliers['Income'].astype('float')
#
# b, m = polyfit(x, y, 1)
# plt.plot(x, y, '.')
# plt.plot(x, b + m * x, '-')

plt.show()
