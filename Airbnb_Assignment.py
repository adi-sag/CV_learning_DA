# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import seaborn as sns
import seaborn as sns2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
#%matplot inline
#%%
df = pd.read_csv(r'C:\Users\aditya194230\Downloads\archive\AB_NYC_2019.csv')

df.head(3)
#%%Understanding, Wrangling and cleaning data
len(df)
df.dtypes
df.isnull().sum() # finding number of nulls in columns
df.drop(['id','host_name','last_review'], axis = 1, inplace = True) # Not relevant


#%%
df.fillna({'reviews_per_month':0},inplace = True)
df.isnull().sum()
df.reviews_per_month.isnull().sum()
#%%
#Finding categorrical unique values
df.neighbourhood_group.unique()
df.neighbourhood.unique()
len(df.neighbourhood.unique())
#%% Exploring and Visualization

#Top host - host with maximum listing on airbnb

Top_host = df.host_id.value_counts().head(10)
Top_host_check = df.calculated_host_listings_count.max()
#%%
sns.set(rc={'figure.figsize':(10,8)})
sns.set_style('white')
#%%
top_host_df = pd.DataFrame(Top_host)
top_host_df.reset_index(inplace=True)
top_host_df.rename(columns = {'index':'Host_ID', 'host_id':'P_Count'},inplace = True)
top_host_df
#%%Bar Plot

viz1=sns.barplot(x="Host_ID", y= "P_Count", data = top_host_df, palette = "Blues_d")
viz1.set_title("Hosts with most listing in NYC")
viz1.set_xlabel("Host IDs")
viz1.set_ylabel("Count of listings")
viz1.set_xticklabels(viz1.get_xticklabels(), rotation = 45)

#%%Violin Plot
sub_1 = df[df.price<800]

viz2 = sns.violinplot(x = 'neighbourhood_group',y = 'price' ,data=sub_1)
viz2.set_title("Density and Distribution of prices for each neighbourhood_group")
viz3 = sns2.violinplot(x = 'neighbourhood_group',y = 'availability_365' ,data=sub_1)
#%%Cat Plot

sub_2 = df.loc[df["neighbourhood"].isin(["Williamsburg","Bedford-Stuyvesant","Harlem","Bushwick","Upper West Side",
               "East Village", "Upper East Side", "Crown Heights","Midtown"])]

viz4 = sns.catplot(x="neighbourhood", hue = "neighbourhood_group", col = 'room_type', data = sub_2,kind = "count")

viz4.set_xticklabels(rotation = 90)
#%% Scatter Plot (latitude and longtitude)

viz4 = sub_1.plot(kind="scatter", x = "longitude", y = "latitude", label = "availability_365", c = "price", cmap = plt.get_cmap("jet"), colorbar = True, alpha = 0.4, figsize = (10,8))
viz4.legend()

#%%
names = []
for name in df.name:
    names.append(name)

def split_name(name):
    spl=str(name).split()
    return spl

names_for_count = []

for x in names:
    for word in split_name(x):
        word = word.lower()
        names_for_count.append(word)
        
names_for_count_1 = [s for s in names_for_count  if s not in ['in','the','for','and','&','of','to','is','are'] ]
      
from collections import Counter 
top_25 = Counter(names_for_count_1).most_common()
top_25 = top_25[0:15]

sub_3 = pd.DataFrame(top_25)
sub_3.rename(columns = {0:"Words", 1:"Count"}, inplace = True)

viz5 = sns.barplot(x="Words", y = "Count", data = sub_3)
viz5.set_title("Count of the top 25 used words for listing names")
#viz5.set_ylable("Count of words")
viz5.set_xlabel("Words")
viz5.set_xticklabels(viz5.get_xticklabels(),rotation = 90)








