
# Name: EnrollPro
# Description: A simple program that find the courses I need to enroll in. The program also checks if the pre-requisites and co-requisites are met.
# it also checks if the course is available in the current study period.
# Version: 1.1 - GUI
# Date: 15/01/2022
# Date of update: 20/01/2023
# update: added a GUI
# Author: Taqi Khaliqdad

# external modules used:
from tqdm import tqdm
from termcolor import colored
import time
import tkinter as tk

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

root = tk.Tk()
root.title("EnrollPro") 
root.geometry("1500x900")


# courses available in study period 2:
def studyPeriod2():
    blank = tk.Label(root, text=" ", font=("Arial", 14))
    blank.pack()
    mainHeading = tk.Label(root, text="Courses available in study period 2:", font=("Arial", 14))
    mainHeading.pack()

    for course in study_periods[2]:
        courseCode = tk.Label(root, text=course, font=("Arial", 10), fg="black", bg="white", padx=10, pady=10, relief="solid")
        # show the label in one line:   
        courseCode.pack(side="top", fill="x")
        # show the label in a new line:
        courseCode.pack()



studyPeriod2()
# courses available in study period 5:
root.mainloop()

