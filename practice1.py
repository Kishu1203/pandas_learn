import pandas as pd
import numpy as np
import random

# Lists
'''
data = [ ['Alice', 20, 'A', 'New York'], ['Bob', 21, 'B', 'Chicago'], ['Charlie', 19, 'A', 'Boston'] ]
df = pd.DataFrame(data, columns=['name', 'age', 'grade', 'city'])
print(df)
'''

# dictionaries
'''
student_data = { 'name': ['Alice', 'Bob', 'Charlie', 'Diana'], 'age': [20, 21, 19, 22], 'grade': ['A', 'B', 'A', 'B'], 'city': ['New York', 'Chicago', 'Boston', 'Miami'] }
df = pd.DataFrame(student_data) 
print(df)
'''


#arrays
'''
ages = np.array([20, 21, 19, 22, 23]) 
df = pd.DataFrame(ages, columns=['Age'])  
print(df)
'''


df= pd.read_csv('titanic.csv')

df.head()  # Display the first few rows of the DataFrame