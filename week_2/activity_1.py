'''
Activity-1: Dropping Unwanted Columns
Description : Usually, a given task only depends on a few columns of data, and the rest of columns can be dropped to save memory. In this Activity, you need to get rid of unwanted columns in the above dataset:

'Edition Statement',
'Corporate Author',
'Corporate Contributors',
'Former owner',
'Engraver',
'Contributors',
'Issuance type',
'Shelfmarks'
Steps :

Load the dataset into a dataframe
Print the columns of the dataset, and print the dataset to be familiar with the data
Calculate and print the number of nan (not a number) in each column
Drop the columns of dataframe by the above-mentioned black list
Print the columns of the dataset to make sure the dataframe includes only desired columns
'''

import pandas as pd


def read_data(_path):
    return pd.read_csv(_path)


def print_columns(_df):
    print(_df.columns.values.tolist())


def print_na(_df):
    print(_df.isna().sum())


def delete_cols(cols, _df):
    return _df.drop(columns=cols)


path = './data/book.csv'
df = read_data(path)
print_columns(df)
print_na(df)
to_delete_columns = ['Edition Statement',
'Corporate Author',
'Corporate Contributors',
'Former owner',
'Engraver',
'Contributors',
'Issuance type',
'Shelfmarks']
df = delete_cols(to_delete_columns, df)
print_columns(df)
