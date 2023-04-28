# =================================================================================================================
# ; Title: Exercise 7.3 - Python with MongoDB, Part 2
# ; Author: Brett Grashorn
# ; Bellevue University
# ; Date: 04/27/2023
# ; Description: In this exercise learn to use Python to connect to MongoDB
# ; Work Cited:
#   Python for Beginners https://www.youtube.com/watch?v=kqtD5dpn9C8&t=3594s
#   Web 335 Exercise 7
#   Web 335 Python Guide
# =================================================================================================================

from pymongo import MongoClient
import datetime

#  build a connection string
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@bellevueuniversity.3x5untt.mongodb.net/web335DBretryWrites=true&w=majority")

# configure a variable to access the web335DB
db = client["web335DB"]

print(client)

# Creating new user document
brett = {
    "firstName": "Brett",
    "lastName": "Grashorn",
    "employeeId": "1221",
    "emailAddress": "brett@me.com",
    "dateCreated":  datetime.datetime.utcnow()
}

# Adding the document ot the users collection
brett_user_id = db.users.insert_one(brett).inserted_id
print(brett_user_id)

# Verification that new user was added to collection
print(db.users.find_one({"employeeId": "1221"}))

# Updating email address
db.users.update_one(
    {"employeeId": "1221"},
    {
        "$set": {
            "emailAddress": "bgrashorn@email.com"
        }
    }
)

# Verification email address was added
print(db.users.find_one({"employeeId": "1221"}))

# Deleting new user we created.
result = db.users.delete_one({
    "employeeId": "1221"
})

# Print results of query
print(result)

# Verification
print(db.users.find_one({"employeeId": "1221"}))
