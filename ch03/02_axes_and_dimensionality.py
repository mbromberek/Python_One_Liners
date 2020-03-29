import numpy as np

a = np.array([1, 2, 3, 4])
print(a.ndim)
# 1

b = np.array([[2, 1, 2], [3, 2, 3], [4, 3, 4]])
print(b.ndim)
# 2

c = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
              [[1, 2, 4], [2, 3, 5], [3, 4, 5]]]
)
print(c.ndim)
# 3

print()

d = np.array([1, 2, 3, 4])
print(d)
print(d.shape)
# 4

e = np.array([[2, 1, 2], [3, 2, 3], [4, 3, 4]])
print(e)
print(e.shape)
# (3, 3)

f = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
              [[1, 2, 4], [2, 3, 5], [3, 4, 6]]]
)
print(f)
print(f.shape)
# (2, 3, 3)
print(f.dtype)

print()

g = np.array([1, 2, 3, 4], dtype=np.int16)
print(g) # [1 2 3 4]
print(a.dtype) #int16

h = np.array([1, 2, 3, 4], dtype=np.float64)
print(h)
print(h.dtype) # float64

