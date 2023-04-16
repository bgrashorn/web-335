#
#     Title: grashorn_hobbies.py
#     Author: Brett Grashorn
#     Date: 15 April 2023
#     Description: File for Exercise 5.3. Python Conditionals, Lists, and Loops
#     using Python.
#     Sources: WEB-335
#     W3 Schools
#

""" String Array of Hobbies """
hobbies = ["Video Games", "Baseball Cards",
           "Lifting Weights", "Golf", "Reading"]

""" For loop that iterates the list and prints them """
for hobby in hobbies:
    print(hobby)

""" String Array of Days """
days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]

""" For Loop with if else statement """
for day in days:
    if day == "Sunday":
        print("It's Sunday! That means no work and you can enjoy your hobbies!")
    elif day == "Monday":
        print("It's Monday and you have to work.")
    elif day == "Tuesday":
        print("It's Tuesday and you have to work.")
    elif day == "Wednesday":
        print("It's Wednesday and you have to work.")
    elif day == "Thursday":
        print("It's Thursday and you have to work.")
    elif day == "Friday":
        print("It's Friday and you have to work.")
    elif day == "Saturday":
        print("It's Saturday! That means no work and you can enjoy your hobbies!")
