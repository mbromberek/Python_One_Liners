import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
)

indices = np.array([[False, False, True],
                    [False, False, False], 
                    [True, True, False]]
)

print(a[indices])
# [3 7 8]


print('\nListing 3-17')
## Data: popular Instagram accounts (millions followers) 
inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"], 
                 [59, "@victoriassecret"], 
                 [120, "@cristiano"], 
                 [111, "@beyonce"], 
                 [76, "@nike"]]
)

## One-liner
superstars = inst[inst[:,0].astype(float) >100, 1]

## Results
print(superstars)
