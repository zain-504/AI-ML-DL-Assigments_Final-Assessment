import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Week 4/FastFoodRestaurans.csv', delimiter= ',', parse_dates= [2],)

long , lat = np.genfromtxt('Week 4/FastFoodRestaurans.csv', delimiter=';', usecols=(4,5), unpack=True, dtype=None)


print(data)

print(long)
# print(keys)
# print(postalCode)
print(lat)

# Applying Numpy Attributes

print (data.ndim)
print (data.shape)
print (data.dtypes)
print (data.max)
print (data.sum)
print (data.size)

# Applying Sorting mathods of Numpy

user = input("Your are going to apply sorting mathods-----")
data_cleaned = data.fillna("unknown")
# np.sort(data)
# np.argmax(data)
# np.argmin(data)
# np.where(data)


# Array Creation Method 

# random_column = np.random.rand(len(data)),np.arange(data)
np.array(data)
np.zeros(data)
np.empty(data)
