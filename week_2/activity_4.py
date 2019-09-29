'''
Activity-4: Merging Two Dataframes
Description : There are times that you need to merge/join two or more datasets to get information you need. In this activity, using a new toy dataset, you will find publication count by country ( how many books are published in each country) . Since the given dataset dose not provide the country of publication, we use City.csv to map cities to countries.

Steps :

Load the Books dataset into a dataframe
Apply the cleansing methods discussed in Activity-2 to the dataframe
Replace the spaces in the column names with the underline character ('_')
Load the City dataset into a dataframe
Merge two datasets based on the name of city
Group by the resultant dataframe based on the country column
While grouping by, to keep the name of countries set as_index=False
Use count() to calculate the number of publications by country.
Print the dataframe
'''

import pandas as pd


def change_name(data):
    if 'London' in data['Place of Publication']:
        data['Place of Publication'] = 'London'
        return data
    else:
        return data.replace('-', ' ')


def change_name2(data):
    if 'London' in data:
        return 'London'
    else:
        return data.replace('-', ' ')


df = pd.read_csv('./data/book.csv')
df = df.apply(change_name, axis=1)
# or
# df['Place of Publication'] = df['Place of Publication'].map(change_name2)


def change_date(data):
    str_data = str(data)
    ret_list = []
    counter = 0
    for i in str_data:
        if counter > 3:
            return ''.join(ret_list)
        if i.isdigit():
            ret_list.append(i)
            counter+=1
    return ''.join(ret_list)

df['Date of Publication'] = df['Date of Publication'].map(change_date)


def change_date_int(data):
    try:
        return int(data)
    except:
        return 0
df['Date of Publication'] = df['Date of Publication'].map(change_date_int)

print(df['Date of Publication'])


def print_dataframe(dataframe, print_column=True, print_rows=True):
    # print column names
    if print_column:
        print(",".join([column for column in dataframe]))

    # print rows one by one
    if print_rows:
        for index, row in dataframe.iterrows():
            print(",".join([str(row[column]) for column in dataframe]))


df.columns = [c.replace(' ', '_') for c in df.columns]
city = pd.read_csv('./data/City.csv')
c = pd.merge(df, city, how='left', left_on='Place_of_Publication', right_on='City')
print(c.groupby('Country', as_index=False)['Identifier'].count())

