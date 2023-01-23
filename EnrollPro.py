
# Name: EnrollPro
# Description: A simple program that find the courses I need to enroll in. The program also checks if the pre-requisites and co-requisites are met.
# it also checks if the course is available in the current study period.
# Version: 1.0
# Date: 15/01/2022
# Author: Taqi Khaliqdad

# external modules used:
from tqdm import tqdm
from termcolor import colored
import time
import datetime

# list of all the courses I need to enroll in:

courseCodes = ['INFT 1016', 'COMP 1039', 'INFT 1012', 'INFT 1030', 'INFS 1025', 'INFS 1026', 'INFT 1031',
               'COMP 1046', 'INFS 2044', 'INFS 2045', 'INFS 3090', 'INFS 2041', 'INFS 2043', 'INFS 4020',
               'INFT 3033', 'COMP 2035', 'COMP 2012', 'INFS 2011', 'ELECTIVE', 'INFT 2064', 'COMP 3023',
               'COMP 2019', 'INFT 3043', 'ICT PROJECT']

# a dictionary of course codes and their associated names:
courseNames = {
    'INFT 1016': 'Information Technology Fundamentals',
    'COMP 1039': 'Problem Solving and Programming',
    'INFT 1012': 'Networking Fundamentals',
    'INFT 1030': 'Design Thinking Studio',
    'INFS 1025': 'Data Driven Web Technologies',
    'INFS 1026': 'System Requirements & User Experience',
    'INFT 1031': 'System Requirements Studio',
    'COMP 1046': 'Object Oriented Programming',
    'INFS 2044': 'System Design & Realisation',
    'INFS 2045': 'System Design Studio',
    'INFS 3090': 'Security Foundations',
    'INFS 2041': 'Agile Development & Governance',
    'INFS 2043': 'Project Studio',
    'INFS 4020': 'Big Data Concepts',
    'INFT 3033': 'IOS Enterprise Development',
    'COMP 2035': 'Operating Systems & Tool Chains',
    'COMP 2012': 'Data Structures Essentials',
    'INFS 2011': 'Database For The Enterprise',
    'ELECTIVE':  'Elective',
    'INFT 2064': 'Web Technologies',
    'COMP 3023': 'Design Patterns with C++',
    'COMP 2019': 'AI & Machine Learning',
    'INFT 3043': 'Cloud & Concurrent Programming',
    'ICT PROJECT': 'ICT Project'
}
 
# list of courses I have already enrolled & passed:

passedCourses = set(['INFT 1016', 'COMP 1039', 'INFT 1012', 'INFT 1030', 'INFS 1025', 'INFS 1026', 'INFT 1031'])

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

# Courses with Co-requisites:
coRequisites = {
        "INFS 2045": "INFS 2044",
        "INFS 2043": "INFS 2041",
        "INFT 2064": "COMP 2012"
}

# Courses in each study periods:
study_periods = {
    # courses available in study period 2:

    2: ['INFT 1016', 'COMP 1039', 'INFT 1012', 'INFT 1030', 'INFS 1025', 'INFS 1026', 'INFT 1031',
            'COMP 1046', 'INFS 2044', 'INFS 2045', 'INFS 3090', 'INFS 4020', 'COMP 2035', 'COMP 2012',
            'INFS 2011', 'ELECTIVE', 'COMP 3023', 'ICT PROJECT'],
    
    # courses available in study period 5:

    5: ['INFS 2041', 'INFS 2043', 'INFT 3033', 'INFT 2064', 'COMP 2019', 'INFT 3043']
}

# courses to enroll in:
coursesToEnroll = []

# function starts here

def checkPreRequisites(course): # function to check if the pre-requisites are met
    if course in preRequisites:
        if preRequisites[course] in passedCourses or preRequisites[course] in coursesToEnroll:
            print()
            print("     ✓ Pre-requisite met")
            print()
            return True
        else:
            print("     ✕ Pre-requisite not met")
            return False

def checkCoRequisites(course): # function to check if the co-requisites are met
    if course in coRequisites:
        if coRequisites[course] in coursesToEnroll:
            print("     ✓ Co-requisite met")
            print()
            return True
        else:
            print("     ✕ Co-requisite not met")
            print("     Δ You need to enroll in ", coRequisites[course], "first.")
            print()
            return False
    else:
        return True

def checkStudyPeriod(course): # function to check if the course is available in the study period

    study_period = int(input("     Enter the study period (2 or 5): "))

    while study_period != 2 and study_period != 5:
        study_period = int(input("     Please enter a valid study period: "))
        print()

    if course in study_periods[study_period]:
        print("     ✓ Course is available in study period", study_period)
        print()
        return True

    else:
        print("     ✕ Course is not available in study period", study_period)
        return False

def Enrollments():

    # print all the courses in the list except the ones already passed  
    print("     Available courses: ")
    for course in courseCodes:
        if course not in passedCourses:
            if course not in coursesToEnroll:
                print("    ", course + ":", courseNames[course])
            
    print()
    userInput = input("     Enter the course code: ") # user input is the course code asked for
    

    if userInput.islower(): # if the user input is in lower case, it will be converted to upper case as per the course code format
        userInput = userInput.upper()

    while userInput not in courseCodes:
        print("     Δ Course not found")
        print()
        userInput = input("     Please enter a valid course code: ")
        userInput = userInput.upper()

    if userInput in courseCodes:
        if userInput in passedCourses:
            print("     ✓ You have already passed ", userInput)

        elif userInput in coursesToEnroll:
            print("     ✓ You have already added ", userInput, "to the list.")

        else:
            if checkPreRequisites(userInput) and checkCoRequisites(userInput) and checkStudyPeriod(userInput):
                coursesToEnroll.append(userInput)

                # the following code is to show a progress bar just for fun

                i = 0
                while i < 100:
                    i += 1
                    print("     Adding...", i, "%", end="\r")
                    time.sleep(0.01)

                print()
                print("     ✓ ", userInput,  "added to the list.")
                print()
            else:
                print("     ✕ Course not added to the list.")
                print()

name = "EnrollPro"
version = "1.0"
print(colored("*"*50, "blue"))
print(colored("{:^50}".format("Welcome to the {} program".format(name)), "green"))
print(colored("{:^50}".format("Version: {}".format(version)), "green"))
print(colored("*"*50, "blue"))
print()

userExits = False
while userExits != True:

    Enrollments()

    userExits = input("     Do you want to continue? (Y/N): ")
    print()
    while userExits != "Y" and userExits != "N" and userExits != "y" and userExits != "n":
        userExits = input("     Please enter Y or N: ")

    if userExits == "N" or userExits == "n":
        userExits = True
        
        if len(coursesToEnroll) == 0:
            print()
            print("     You have not added any courses to the list 🤷")
            print()
            input("     Press enter to close!")
            break   
        else:
            print("     Enroll in the following courses: ")
            print("     =================================")
            print()

            # Outputting the list of courses in a nice square

            print(colored("     +" + "-"*48 + "+", "yellow"))

            for i, course in enumerate(coursesToEnroll):
                print(colored("     | {:<47}|".format(str(i+1) + "-> " + courseNames[course] + str(" (") + course + str(")") , "white")))
            print(colored("     +" + "-"*48 + "+", "yellow"))

            askUser = input("     Do you want to save the list to the file? (Y/N): ")
            if askUser == "Y" or askUser == "y":
                print()
                TextFile = open("EnrolledCourses.txt", "w")
                TextFile.write("Enroll in: " + "\n")
                TextFile.write("===========" + "\n")
                index = 1
                for course in coursesToEnroll:
                    TextFile.write(str(index) + ". " + courseNames[course] + " (" + course + ")" + "\n")
                TextFile.close()

                print("     List saved successfully!")
                print()
                input("     Press enter to close!")
