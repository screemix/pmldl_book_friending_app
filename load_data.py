import json
import numpy as np
import pymongo

with open('books.json', 'r') as f:
    data = json.load(f)
f.close()

with open('monogo_connection_string', 'r') as f:
    conn_string = f.readline()
f.close()

myclient = pymongo.MongoClient(conn_string)
mydb = myclient["test"]


books_col = mydb["books"]
users_col = mydb['users']

books_col.insert_many(data)
