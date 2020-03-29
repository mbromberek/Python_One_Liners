## Dependencies
import numpy as np

'''
How do we find the maximum after-tax income in a group of people, given their yearly salary and tax rates
'''

## Data: yearly salary in ($1000) [2017, 2018, 2019]
alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]

salaries = np.array([alice, bob, tim])
taxation = np.array([[0.2, 0.25, 0.22],
                     [0.4, 0.5, 0.5],
                     [0.1, 0.2, 0.1]])

## One-liner
max_income = np.max(salaries - (salaries * taxation))

print(max_income)


print('\nExercise 3-1')
employees = ['Alice', 'Bob', 'Tim']
print(np.nonzero(salaries == np.max(salaries)))

max_income_employee = employees[np.nonzero(salaries == np.max(salaries))[0][0]]
print(max_income_employee)
