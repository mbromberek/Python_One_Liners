import numpy as np

x = np.array([[1, 0, 0], 
              [0, 2, 2], 
              [3, 0, 0]])
print('\nListing 3-12')
print(np.nonzero(x))
# Returns (array([0, 1, 1, 2]), array([0, 1, 2, 0]))
# tuple of two NumPy arrays. First array gives the row indices and the second gives the column indices of the non zero elements. 

# y = np.nonzero(x)
# print(y[0][0], y[1][0])
# print(x[y[0][3], y[1][3]])
print('\nListing 3-13')

print(x == 2)
"""
[[False False False]
 [False  True  True]
 [False False False]]
"""

print('\nListing 3-14')
## Data: air quality index AQI data (row = city)
X = np.array(
    [[ 42, 40, 41, 43, 44, 43 ], # Hong Kong 
    [ 30, 31, 29, 29, 29, 30 ], # New York 
    [ 8, 13, 31, 11, 11, 9 ], # Berlin 
    [ 11, 11, 12, 13, 11, 12 ]] # Montreal
)

cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

print('Average AQI: ' + str(np.average(X)))
print(X >= np.average(X))

print(np.nonzero(X > np.average(X)))

## One-liner
polluted = set(cities[np.nonzero(X > np.average(X))[0]])

## Result
print(polluted)

"""
We convert the list of cities into a set since that removed the duplicates
"""
