
from sklearn.linear_model import LinearRegression
import numpy as np


# my grades from the first year of university   

grades = ['D', 'C', 'C', 'C', 'C']

# use the above module, and the grades to predict my second year grades 

# create a dictionary to map the grades to numbers

gradeDict = {'HD': 85, 'D': 75, 'C': 65, 'P': 50, 'F': 49}

# use the gradeDict to map the grades to numbers

gradeNum = [gradeDict[grade] for grade in grades]

# create a list of the years

years = [1, 2, 3, 4, 5]

# use the years, grades, and the gradeDict to predict my grades in the second year  

# create a numpy array of the years

# reshape the input variables

years = np.array(years).reshape(-1,1)
gradeNum = np.array(gradeNum).reshape(-1,1)

# create an instance of the linear regression model
reg = LinearRegression().fit(years, gradeNum)

# use the model to make predictions
predicted_gradeNum = reg.predict(np.array([[2]]))

print(predicted_gradeNum)


