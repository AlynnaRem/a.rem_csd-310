# Alynna Rem. 4/10/2022. Module 5.3 Assignment: PyTech: Collection Queries
# pytech_queries.py
# Querying the student collection for existing documents

# import statement
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.nfhlx.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the student collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# find document by student_id
rem = students.find_one({"student_id": "1007"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + rem["student_id"] + "\n  First Name: " + rem["first_name"] + "\n  Last Name: " + rem["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
