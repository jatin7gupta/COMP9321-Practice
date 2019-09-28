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
