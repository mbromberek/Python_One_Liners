'''
Have data for a variety of professions, and you want to increase the salaries of just the data scientists by 10 percent every other year. 
'''

## Dependencies
import numpy as np

## Data: yearly salary in ($1000) [2025, 2026, 2027]
dataScientist = [130, 132, 137]
productManager = [127, 140, 145]
designer = [118, 118, 127]
softwareEngineer = [129, 131, 137]

employees = np.array([dataScientist, productManager, designer, softwareEngineer])
print(employees)

## One-liner
employees[0,::2] = employees[0,::2] * 1.1

##Results
print(employees)
print(employees.dtype)

'''
The One-liner uses slices to get every other value of the first row of the array

Broadcasting is used to automatically fix element-wise operations since the right of the operator (*) is a float and the left of the operator is an array. So it makes the float an array of copies of itself. This makes the computation look more like np.array([130, 137]) * np.array([1.1, 1.1])

Array Types - The resulting employees data type is still an int64 after the multiplication with a floating point number, this is due to the data type of the array being unchangeable 

'''