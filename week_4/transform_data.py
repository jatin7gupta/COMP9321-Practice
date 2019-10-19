import pandas as pd


def transform(df):
    columns_to_drop = ['Edition Statement',
                       'Corporate Author',
                       'Corporate Contributors',
                       'Former owner',
                       'Engraver',
                       'Contributors',
                       'Issuance type',
                       'Shelfmarks'
                       ]

    df.drop(columns_to_drop, inplace=True, axis=1)

    df['Place of Publication'] = df['Place of Publication'].apply(
        lambda x: 'London' if 'London' in x else x.replace('-', ' '))

    new_date = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)

    # ^(\d{4}) : matches 4 digit numbers in the beginning of the string
    new_date = pd.to_numeric(new_date)

    # replace all NaN with 0
    new_date = new_date.fillna(0)
    df['Date of Publication'] = new_date

    # Set the index of the loaded dataframe to be the "Identifier" column this will help us to find books with their ids
    df.set_index('Identifier', inplace=True)

    # Replace the spaces in the column names
    df.columns = df.columns.str.replace(' ', '')
    return df
