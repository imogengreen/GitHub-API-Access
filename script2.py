# a script to do python based access to the github api
import pymongo              # for mongodb access
import pprint               # for pretty printing db data

# print("Demonstration python based mongodb access");

# Let's get the user object from the db
# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
database = client.classDB

for user in database.githubuser.find({'location': {'$exists': True}}):
    pprint.pprint(user)
    print()
