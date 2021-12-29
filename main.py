# This is a sample Python script.
from github import Github
import json
import pymongo

g = Github("token")

user = g.get_user()

dct = {'user': user.login,
       'fullname': user.name,
       'company': user.company,
       'location': user.location,
       'followers': user.followers,
       'following': user.following,
       'public repositories': user.public_repos,
       'private repositories': user.total_private_repos
       }

def compileLanuages(repoAddress):
       repo = g.get_repo(repoAddress)
       languages = repo.get_languages()
       return languages

print("dictionary is " + json.dumps(dct))

for k, v in dict(dct).items():
       if v is None:
              del dct[k]

print("cleaned dictionary is " + json.dumps(dct))

# create connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# create the database (we could instead dump this into a JSON file)
database = client.classDB
database.githubuser.insert_many([dct])
