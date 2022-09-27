# -*- coding: utf-8 -*-
#### PANDAS PRACTICE 
################### PANDAS SERIES ##############################

import numpy as np
import pandas as pd

#print(np.__version__)
#print(np.show_config())

#Compare Sries elements
df1 = pd.Series([1,2,3,4])
df2 = pd.Series([1,2,3,4])
#print(df1 == df2)

# Dict to Series
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
series_d1 = pd.Series(d1)
print(series_d1)
#%%
# Numpy array  to Series

x = [12,3,45]
z=np.array([2,3,4,5])
y= pd.Series(x)
print(pd.Series(z))
print(y)

#%% Series to Array 
s1 = pd.Series([1,2,3,'ads'])
s2 = np.array(s1.values.tolist())
print(s2)

#%% Change data type of given a column or a Series

s1 = pd.Series([1,3,5.0,'python', 'sql'])

s2 = pd.to_numeric(s1,errors="coerce")
#coerce overwites the string with NaN
#raise will throw error
print(s2)
#%%Sort values in series
a1 = pd.Series([1,2486,74923,35,67])
a2 = pd.Series(['adi','imos','ui',"ewi"])
print(a1.sort_values())
print(a2.sort_values())
#%%Append data to existing series
w = pd.Series([45,67,4])

print(a1.append(w))
print(a1.append(w,True)) # true is to reset index
#%%

######################### PANDAS DATAFRAMES ################################

DF11 = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})

#print(DF11.loc(2,2)) 

#%% Sumary of Dataframe 

DF11.info()
#%% Working on Selection practice
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df21 = pd.DataFrame(exam_data , index=labels)
#print(df21.iloc[2:])
print(df21[['name','score']])
print(df21['name'])

#%% Select * from df21 where attempts >2

print(df21[df21['attempts']>2]) #select * with where clause
print(df21['attempts']>2) #returns series of True and False
#%% Sum of attempts 
print(df21['attempts'].sum())
#other functions - 
print(df21['score'].mean())
#%% Sort by name descending order and score by ascending order 
# Data frames are mutable, executing below command with ovrride df21.
#df21.sort_values(by=['name', 'score'], ascending=[False, True])

df22 = df21.sort_values(by=['name', 'score'], ascending=[False, True])

print(df22) 

#%% In qualify col - replace yes and no with True or False 

df21['qualify_2'] = df21['qualify'].map({'yes': True, 'no': False})
print(df21) 

#change name from James to Suresh

print("\nChange the name 'James' to ‘Suresh’:")
df21['name'] = df21['name'].replace('James', 'Suresh')

#drop column

df21.drop('qualify',1) # 1 stands for axis = 1 i.e., vertically.
#%% Change column sequence

d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}

df22 = pd.DataFrame(d)

df22 = df22[['col3','col1','col2','col1']]

print(df22)

#%%Group by

df12 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
g1 = df12.groupby(['city'])
print(g1.count())

#%%Group by another example 
#result = orders_data.groupby('customer_id').agg({'purch_amt': ['mean', 'min', 'max']})

#%%  
###############PANDAS JOINING DATAFRAME###############################

student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})


student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})

result_data = pd.concat([student_data1, student_data2])# along row

result_data_2 = pd.concat([student_data1, student_data2], axis = 1) # along column

#%% Concate series to existing dataframe
s6 = pd.Series(['S6', 'Scarlette Fisher', 205], index=['student_id', 'name', 'marks'])
combined_data = student_data1.append(s6, ignore_index = True)

#%% Perform Join 

exam_data = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
        'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]})

Final_merged = pd.merge(result_data,exam_data, on = 'student_id') #option available for join type - "how = 'inner'"
# for multiple keys in join use -> on = [<set of keys sperated by comma>]

# To merge by ignoring index col names use, we can call this as UNION ALL
#result = pd.concat([data1,data2], axis=0, ignore_index=True)

#%% 
################## LIST ###############################

A = [10,20,30] 
b=[[1.1,1.2,1.3,1.4], [2.1,2.2,2.3,2.4,2.5]]
# for i in A:
#     print (i)
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j])
    #print("I m exiting:", i)
### Range must be used when iterating over list of list, len won't work. 
#IF you want to use len then start and end also needed. 

#%% Adding data to existing list
A.append(1)
C = [20,20,20]
A.append(C) #APPENDING list as an single element to a list. 
##### Using INSERT ####
A.insert(3, C)  
####  Extend ######
A.extend(C)  
#%% Elements can be accessed using negative index
## REmoving elements from List
A.remove([20,20,20])
print(A)
A.remove(1) 
# Remove 1st occurence of element
#%% USING pop element ####
A.pop()  
print(A)
A.pop(2) #remove element at 2nd index position i.e. 3rd element
print(A)

#%% TO clear all elements from LIST 

A.clear()
A.reverse()

#%%

# List of strings
l = ['sat', 'bat', 'cat', 'mat']
  
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
#%%
# Return double of n
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
#%%
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))
#%%
#Enumerate 

'''enumerate(iterable, start=0)

Parameters:
Iterable: any object that supports iteration
Start: the index value from which the counter is 
              to be started, by default it is 0'''

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
  
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
  
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
  
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))




































