#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Problem:
# 有 x、y、z 三個活動想在同一天舉辦
# 場地總時間只有四個小時可使用
# 活動 z 的價值為活動 x 及 y 的兩倍
# 活動 x 與活動 y 至少要選一個舉辦
# 活動 x 需花費1小時
# 活動 y 需花費2小時
# 活動 z 需花費3小時
# 舉辦哪幾個活動可以使價值最大化?


# In[6]:


# maximize x+y+2z
# subject x+2y+3z<=4
#         x+y>=1
#         x,y,z binary


# In[2]:


from pulp import *
model = pulp.LpProblem("value max", pulp.LpMaximize)
x = pulp.LpVariable('x',lowBound = 0, cat='Binary')
y = pulp.LpVariable('y',lowBound = 0, cat='Binary')
z = pulp.LpVariable('z',lowBound = 0, cat='Binary')

model += x+y+2*z


model += x+2*y+3*z <= 4
model += x+y >= 1

model.solve()


for v in model.variables():
    print(v.name, "=", v.varValue)
    

print('obj=',value(model.objective))


# In[ ]:




