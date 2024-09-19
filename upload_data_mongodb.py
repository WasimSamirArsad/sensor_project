from pymongo import MongoClient
import pandas as pd
import json

uri="mongodb+srv://wasim:wasim@cluster0.xwvl1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client

client=MongoClient(uri)

# crate database and collection name

DATABASE_NAME="WASIM"
COLLECTION_NAME="waferfault"

# read datasets

df=pd.read_csv("notebook/wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_records=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)

