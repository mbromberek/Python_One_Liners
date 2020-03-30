import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a.reshape((2, 3)))
'''
[[1 2 3]
 [4 5 6]]
'''

print(a.reshape((2, -1)))
'''
[[ 1 2 3]
  [4 5 6]]
The shape value -1 for the column argument indicates that NumPy should replace it with the correct number of columns 
'''

# daily stock prices
# [monday, midday, evening]
solar_x = np.array(
    [[1, 2, 3], # today
     [2, 2, 5]] #yesterday
)

# midday - weighted average
print(np.average(solar_x, axis=0))
# [1.5 2. 4.]

