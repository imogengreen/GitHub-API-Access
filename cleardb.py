
# a a script to clear the db
# step 7 - Let's do a useful search
import pymongo              # for mongodb access
import pprint               # for pretty printing db data

print("Demonstration python based mongodb access")

# Let's get the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
database = client.classDB

database.githubuser.delete_many({})
