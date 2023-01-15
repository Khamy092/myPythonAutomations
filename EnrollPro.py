
# Name: EnrollPro
# Description: A simple program that find the courses I need to enroll in
# Date: 15/01/2022
# Author: Taqi Khaliqdad


# function starts here

# list of all the courses I need to enroll in:

courseCodes = ['INFT 1016', 'COMP 1039', 'INFT 1012', 'INFT 1030', 'INFS 1025', 'INFS 1026', 'INFT 1031',
               'COMP 1046', 'INFS 2044', 'INFS 2045', 'INFS 3090', 'INFS 2041', 'INFS 2043', 'INFS 4020',
               'INFT 3033', 'COMP 2035', 'COMP 2012', 'INFS 2011', 'ELECTIVE', 'INFT 2064', 'COMP 3023',
               'COMP 2019', 'INFT 3043', 'ICT PROJECT']

# list of courses I have already enrolled & passed:

enrolledCourses = [(courseCodes[0], courseCodes[1], courseCodes[2], courseCodes[3], courseCodes[4], courseCodes[5], courseCodes[6],)]

# Course Pre-requisites:

INFT1016, COMP1039, INFT1012, INFT1030, INFS1025, INFS1026, INFT1031 = None
COMP1046 = [COMP1039] ; INFS2044 = [INFT1031, COMP1039]
INFS2045 = [INFT1031] ; INFS3090 = [INFT1012, INFT1016] ; INFS2041 = [INFS2045]
INFS2043 = [INFS2045] ; INFS4020 = [INFS1025]



# Course Co-requisites:
courseCoReq = []
CourseA = INFS2045 = [INFS2044]
CourseB = INFS2043 = [INFS2041]
