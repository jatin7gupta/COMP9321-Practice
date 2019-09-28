'''
Activity-2: Cleaning Columns
Description : As you can also see here, some of the columns are not of uniformed format. For example: the "Place of Publication" column contains entries such as: ( "London", "London]" , "London; Virtue & Yorston") which all refer to the same place. In this activity, you are supposed to clear and uniform the entries for two columns: "Place of Publication" and "Date of Publication".

Steps :

Load the dataset into a dataframe
Replace the cell value of "Place of Publication" with "London" if it contains "London", and replace all '-' characters with space
Keep the first 4 digit number in "Date of Publication"
Convert "Date of Publication" cells to numbers
Replace NaN with 0 for the cells of "Date of Publication"
Print the dataframe to see if the changes have been applied properly


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
