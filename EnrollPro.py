
# Name: EnrollPro
# Description: A simple program that find the courses I need to enroll in
# Date: 15/01/2022
# Author: Taqi Khaliqdad

from tqdm import tqdm
import time
# list of all the courses I need to enroll in:

courseCodes = ['INFT 1016', 'COMP 1039', 'INFT 1012', 'INFT 1030', 'INFS 1025', 'INFS 1026', 'INFT 1031',
               'COMP 1046', 'INFS 2044', 'INFS 2045', 'INFS 3090', 'INFS 2041', 'INFS 2043', 'INFS 4020',
               'INFT 3033', 'COMP 2035', 'COMP 2012', 'INFS 2011', 'ELECTIVE', 'INFT 2064', 'COMP 3023',
               'COMP 2019', 'INFT 3043', 'ICT PROJECT']

# list of courses I have already enrolled & passed:

passedCourses = ['INFT 1016', 'COMP 1039', 'INFT 1012', 'INFT 1030', 'INFS 1025', 'INFS 1026', 'INFT 1031']

# courses with pre-requisites:
preRequisites = {
        "COMP 1046": "COMP 1039",
        "INFS 2044": "INFT 1031",
        "INFS 2045": "INFT 1031" and "COMP 1039",
        "INFS 3090": "INFT 1012" and "INFT 1016",
        "INFS 2041": "INFS 2045",
        "INFS 2043": "INFS 2045",
        "INFS 4020": "INFS 1025",
        "INFT 3033": "COMP 1046",
        "COMP 2035": "COMP 1046",
        "COMP 2012": "COMP 1046",
        "INFS 2011": "INFS 1025",
        "INFT 2064": "INFS 1025" and "COMP 1012",
        "COMP 3023": "COMP 2012",
        "COMP 2019": "COMP1046",
        "INFT 3043": "INFS 1025" and "COMP 2012",
        "ICTPROJECT": 72
    }

# Course Co-requisites:
coRequisites = {
        "INFS 2045": "INFS 2044",
        "INFS 2043": "INFS 2041",
        "INFT 2064": "COMP 2012"
}

# Course study periods:
study_periods = {
    2: ['INFT 1016', 'COMP 1039', 'INFT 1012', 'INFT 1030', 'INFS 1025', 'INFS 1026', 'INFT 1031',
            'COMP 1046', 'INFS 2044', 'INFS 2045', 'INFS 3090', 'INFS 4020', 'COMP 2035', 'COMP 2012',
            'INFS 2011', 'ELECTIVE', 'COMP 3023', 'ICT PROJECT'],
    
    5: ['INFS 2041', 'INFS 2043', 'INFT 3033', 'INFT 2064', 'COMP 2019', 'INFT 3043']
}

# courses to enroll in:
coursesToEnroll = []

# function starts here

def checkPreRequisites(course): # function to check if the pre-requisites are met
    if course in preRequisites:
        if preRequisites[course] in passedCourses:
            print("✓ Pre-requisite met")
            print()
            return True
        else:
            print("✕ Pre-requisite not met")
            return False

def checkCoRequisites(course): # function to check if the co-requisites are met
    if course in coRequisites:
        if coRequisites[course] in coursesToEnroll:
            print("✓ Co-requisite met")
            print()
            return True
        else:
            print("✕ Co-requisite not met")
            return False
    else:
        return True

def checkStudyPeriod(course): # function to check if the course is available in the study period
    study_period = int(input("Enter the study period (2 or 5): "))
    while study_period != 2 and study_period != 5:
        study_period = int(input("Please enter a valid study period: "))
        print()
    if course in study_periods[study_period]:
        print("✓ Course is available in study period", study_period)
        print()
        return True
    else:
        print("✕ Course is not available in study period", study_period)
        return False

def Enrollments():
    print()
    userInput = input("Enter the course code: ") # user input is the course code asked for

    if userInput.islower(): # if the user input is in lower case, it will be converted to upper case as per the course code format
        userInput = userInput.upper()

    while userInput not in courseCodes:
        print("Course not found")
        print()
        userInput = input("Please enter a valid course code: ")

    if userInput in courseCodes:

        if userInput in passedCourses:
            print("You have already passed ", userInput)

        elif userInput in coursesToEnroll:
            print("You have already added ", userInput, "to the list")

        else:
            if checkPreRequisites(userInput) and checkCoRequisites(userInput) and checkStudyPeriod(userInput):
                coursesToEnroll.append(userInput)
                for i in tqdm (range (101),
                    desc="Loading…",
                    ascii=False, ncols=75):
                    time.sleep(0.01)
                print("✓ ", userInput,  "added to the list")
            else:
                print("✕ Course not added to the list")


userExits = False
while userExits != True:

    Enrollments()

    userExits = input("Do you want to continue? (Y/N): ")
    print()
    while userExits != "Y" and userExits != "N" and userExits != "y" and userExits != "n":
        userExits = input("Please enter Y or N: ")

    if userExits == "N" or userExits == "n":
        userExits = True
        pass

print("Enroll in the following courses: ")
print("=================================")

for course in coursesToEnroll:
    number = 1
    while number < len(coursesToEnroll):
        print(number,"->", course)
        number += 1

print("=================================")

print()
print("Good Luck!")
print()

input("PressT Enter to close!")