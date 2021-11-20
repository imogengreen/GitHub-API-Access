# This is a sample Python script.
from github import Github
import json
import pymongo

g = Github("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")

user = g.get_user()

dct = {'user': user.login,
       'fullname': user.name,
       'company': user.company,
       'location': user.location
       }

print("dictionary is " + json.dumps(dct))

for k, v in dict(dct).items():
       if v is None:
              del dct[k]

print("cleaned dictionary is " + json.dumps(dct))

# store the data

# establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# create the database
database = client.classDB
database.githubuser.insert_many([dct])
