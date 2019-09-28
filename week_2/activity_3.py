'''
Activity-3: Filtering Rows
Description : Likewise it is sometime desirable to filter the rows of the dataset. In this Activity, you are supposed to query the dataframe and filter rows.

Steps :

Load the dataset into a dataframe
Apply the cleansing methods discussed in Activity-2 to the dataframe
Replace the spaces in the column names with the underline character ('_')
Because panda's query method does not work well with column names which contains white spaces
Filter the rows and only keep books which are published in "London" after 1866.
Print the dataframe and validate the result
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
print_dataframe(df[
    (df.Place_of_Publication == 'London') &
    (df.Date_of_Publication > 1866)
  ])