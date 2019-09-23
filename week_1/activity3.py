import json
import pandas as pd
from pymongo import MongoClient


def write(df, host, port, db_name, collection):
    client = MongoClient(host=host, port=port)
    c = client[db_name][collection]
    records = json.loads(df.T.to_json()).values()
    c.insert_many(records)


def read(host, port, db_name, collection):
    client = MongoClient(host=host, port=port)
    c = client[db_name][collection]
    return pd.DataFrame(list(c.find()))


if __name__ == '__main__':
    db_name = 'comp9321'
    port = 27017
    host = 'localhost'

    csv_name = './data/export.csv'
    df = pd.read_csv(csv_name)
    collection = 'Demographic_Statistics'

    # write
    write(df, host, port, db_name, collection)

    # read
    df = read(host, port, db_name, collection)
    print(df)