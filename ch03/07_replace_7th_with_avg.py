## Dependencies
import numpy as np

## Sensor data (Mo, Tu, We, Th, Fr Sa, Su)

tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                5, 3, 3, 4, 3, 4, 6, 
                6, 5, 5, 5, 4, 5, 5]
)

## One-liner
tmp[6::7] = np.average(tmp.reshape((-1, 7)), axis=1)

## Result
print(tmp)

'''
Data arrives in the shape of a one=dimensional array. 
Reshape the tmp array data into a two-dimensional array with seven columns and three rows, making it easier to calculate the average for the 7 days

'''