# Alynna Rem. 4/16/2022. Module 6.2 Assignment: PyTech: Updating Documents
# pytech_update.py
# Updating documents in the Pytech database.

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

# update a document in the student collection using the update_one method. Update the last name to something different than the originally saved for student_id 1007.
db.students.update_one({
    'student_id': '1007'
    }, 
    {
    "$set": 
    {
        'last_name': 'Salihovic'
    }})

# find document by student_id of 1007
rem = students.find_one({"student_id": "1007"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")
print("  Student ID: " + rem["student_id"] + "\n  First Name: " + rem["first_name"] + "\n  Last Name: " + rem["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")