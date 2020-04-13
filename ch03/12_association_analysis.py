## Dependencies 
import numpy as np

## Data: row is customer shopping basket 
## row = [course 1, course 2, ebook 1, ebook 2] 
## value 1 indicates that an item was bought. 
basket = np.array([[0, 1, 1, 0],
                   [0, 0, 0, 1], 
                   [1, 1, 0, 0], 
                   [0, 1, 1, 1], 
                   [1, 1, 1, 0], 
                   [0, 1, 1, 0], 
                   [1, 1, 0, 1], 
                   [1, 1, 1, 1]]
)


'''
Find fraction of customers that bought both ebooks
'''
## One-liner
copurchases = np.sum(np.all(basket[:,2:], axis = 1)) / basket.shape[0]

print(basket[:,2:])
# [[1 0]
#  [0 1]
#  [0 0]
#  [1 1]
#  [1 0]
#  [1 0]
#  [0 1]
#  [1 1]]

print(np.all(basket[:,2:], axis = 1))
# [False False False  True False False False  True]

print(np.sum(np.all(basket[:,2:], axis = 1)))
# 2

## Result
print(copurchases)
# 0.25

'''
Find the two items that were purchased most often together
'''
print('\nFind the two items that were purchased most often together')
## One-liner (broken in two lines;)
copurchases = [(i,j,np.sum(basket[:,i] + basket[:,j] == 2)) for i in range(4) for j in range(i+1,4)]

print(copurchases)

## Result
print(max(copurchases, key=lambda x:x[2]))

# on page 78
