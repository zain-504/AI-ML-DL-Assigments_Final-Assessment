import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr[1])

for arr in arr:
    print(arr)

print("Next Run--------------------")


arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr1.dtype)
print(arr1[1])


print("Next Run--------------------")


arr2 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2.size)
print(arr2.dtype)
print(arr2[0:2])


