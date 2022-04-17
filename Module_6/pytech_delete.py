# Alynna Rem. 4/16/2022. Module 6.3 Assignment: PyTech: Deleting Documents
# pytech_delete.py
# Delete documents from an existing MongoDB collection.

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

# add a new document named reed with student_id 1010
reed = {
        "student_id": "1010",
        "first_name": "Sara",
        "last_name": "Reed",
        "enrollments": [
                        {
                          "term": "Spring 2022",
                          "gpa": "4.0",
                          "start_date": "03/14/2022",
                          "end_date": "05/15/2022",
                          "courses": [
                                      {
                                        "course_id": "123458",
                                        "description": "Database Development and Use",
                                        "instructor": "Professor Woods",
                                        "grade": "A",
                                      },
                                      {
                                        "course_id": "123459",
                                        "description": "Programming with Java",
                                        "instructor": "Professor Payne",
                                        "grade": "A",
                                      }
                                     ]
                        }
                       ]
}

# get the students collection
students = db.students

# add the reed document into the pytech collection using the insert_one() method.
reed_student_id = students.insert_one(reed).inserted_id

# find document by student_id of 1010
reed = students.find_one({"student_id": "1010"})

# display message of student inserted into the students collection with document id number
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(reed_student_id))

# output the results 
print("\n  -- DISPLAYING STUDENT TEST DOC --")
print("  Student ID: " + reed["student_id"] + "\n  First Name: " + reed["first_name"] + "\n  Last Name: " + reed["last_name"] + "\n")

# delete student_id 1010 using the delete_one() method
db.students.delete_one({"student_id": "1010"})

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the student collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")