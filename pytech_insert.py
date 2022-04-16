# Alynna Rem. 4/10/2022. Module 5.3 Assignment: PyTech: Collection Queries
# pytech_insert.py
# Using Python to insert new documents into the PyTech collection


# import statement
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.nfhlx.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# 3 student documents by last name.
# Alynna Rem's data document
rem = {
        "student_id": "1007",
        "first_name": "Alynna",
        "last_name": "Rem",
        "enrollments": [
                        {
                          "term": "Winter 2022",
                          "gpa": "4.0",
                          "start_date": "01/03/2022",
                          "end_date": "03/06/2022",
                          "courses": [
                                      {
                                        "course_id": "123456",
                                        "description": "Foundation of Software Dev",
                                        "instructor": "Professor Woods",
                                        "grade": "A",
                                      },
                                      {
                                        "course_id": "123457",
                                        "description": "Intro to Programming with Python",
                                        "instructor": "Professor Payne",
                                        "grade": "A",
                                      }
                                     ]
                        }
                       ]
}

# Anna Smith's data document
smith = {
        "student_id": "1008",
        "first_name": "Anna",
        "last_name": "Smith",
        "enrollments": [
                        {
                          "term": "Winter 2022",
                          "gpa": "4.0",
                          "start_date": "01/03/2022",
                          "end_date": "03/06/2022",
                          "courses": [
                                      {
                                        "course_id": "123456",
                                        "description": "Foundation of Software Dev",
                                        "instructor": "Professor Woods",
                                        "grade": "A",
                                      },
                                      {
                                        "course_id": "123457",
                                        "description": "Intro to Programming with Python",
                                        "instructor": "Professor Payne",
                                        "grade": "A",
                                      }
                                     ]
                        }
                       ]
}

# John Doe's data document

doe = {
        "student_id": "1009",
        "first_name": "John",
        "last_name": "Doe",
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

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
rem_student_id = students.insert_one(rem).inserted_id
print("  Inserted student record Alynna Rem into the students collection with document_id " + str(rem_student_id))

smith_student_id = students.insert_one(smith).inserted_id
print("  Inserted student record Anna Smith into the students collection with document_id " + str(smith_student_id))

doe_student_id = students.insert_one(doe).inserted_id
print("  Inserted student record John Doe into the students collection with document_id " + str(doe_student_id))

# display exit message
input("\n\n  End of program, press any key to exit... ")