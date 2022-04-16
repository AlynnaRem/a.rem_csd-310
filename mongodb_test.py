# Alynna Rem. 4/10/2022. Module 5.2 Assignment: PyTech: Collection Creation
# mongodb_test.py
# Test program for connecting to a MongoDB Atlas cluster

# Import statement
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.nfhlx.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# show the connected collections 
print("\n -- Pytech COllection List --")
print(db.list_collection_names())

# show an exit message
input("\n\n  End of program, press any key to exit... ")