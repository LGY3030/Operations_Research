#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tsp
t = tsp.tsp([(0,0), (0,1), (1,0), (1,1)])
print(t)

mat = [[  0,   1, 1, 1.5],
       [  1,   0, 1.5, 1],
       [  1, 1.5,   0, 1],
       [1.5,   1,   1, 0]]
r = range(len(mat))

dist = {(i, j): mat[i][j] for i in r for j in r}
print(tsp.tsp(r, dist))
print(type(mat))


# In[2]:


from math import *

def calcDistance(Lat_A, Lng_A, Lat_B, Lng_B):
    EARTH_RADIUS = 6378.137;
    radLat1 = radians(Lat_A)
    radLat2 = radians(Lat_B)
    a=radLat1-radLat2
    b=radians(Lng_A)-radians(Lng_B)
 
    s = 2 * asin(sqrt(pow(sin(a/2),2)+cos(radLat1)*cos(radLat2)*pow(sin(b/2),2)));  
    s = s * EARTH_RADIUS;  
    return s;  

Lat_A=32.060255; Lng_A=118.796877 # 南京
Lat_B=39.904211; Lng_B=116.407395 # 北京
distance=calcDistance(Lat_A,Lng_A,Lat_B,Lng_B)
print("----",distance)


# In[3]:


import numpy as np
import pandas as pd
def readData():
    train = pd.read_csv("Data.csv",encoding="big5")
    return train


# In[10]:


data=readData()
mapping={}
print(data)
for i in range(len(data["科系"])):
    mapping[i]=data["科系"][i]
print(mapping)


# In[5]:


distance = np.zeros(shape=(len(data["科系"]),len(data["科系"])))
print(distance)


# In[6]:


for i in range(len(data["科系"])):
    for j in range(len(data["科系"])):
        if i==j:
            distance[i][j]=0
        else:
            distance[i][j]=calcDistance(data["緯度"][i],data["經度"][i],data["緯度"][j],data["經度"][j])
print(distance)


# In[7]:


distance=list(distance)
r = range(len(distance))
dist = {(i, j): distance[i][j] for i in r for j in r}
ans=tsp.tsp(r, dist)
print(ans)


# In[8]:


print(type(ans))


# In[11]:


for i in range(len(ans[1])):
    print(mapping[i])


# In[ ]:




