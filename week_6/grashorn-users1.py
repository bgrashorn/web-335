# =================================================================================================================
# ; Title: Exercise 6.3 - Python with MongoDB, Part 1
# ; Author: Brett Grashorn
# ; Bellevue University
# ; Date: 04/21/2023
# ; Description: In this exercise learn to use Python to connect to MongoDB
# ; Work Cited:
#   Python for Beginners https://www.youtube.com/watch?v=kqtD5dpn9C8&t=3594s
#   Web 335 Exercise 6
#   Web 335 Python Guide
# =================================================================================================================


""" import the MongoClient"""
from pymongo import MongoClient

""" build a connection string """
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@bellevueuniversity.3x5untt.mongodb.net/web335DBretryWrites=true&w=majority")

""" configure a variable to access the web335DB """
db = client['web335DB']

print(client)

print("List of all documents in the users collection")
# displays a list of all documents
for user in db.users.find():
    print(user)

# separates in terminal
print("Emplyee 1011")
# Displays a document where the employeeId is 1011
print(db.users.find_one({"employeeId": "1011"}))

# separates in terminal
print("lastName: Mozart")
# Displays a document with lastName Mozart
print(db.users.find_one({"lastName": "Mozart"}))
