#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# 作業目標<br>
# 讀取存取陣列資料<br>
# 作業重點<br>
# 多陣列存一起需要存成npz，讀取須注意npz中有多個陣列

# 題目:<br>
# 1. 將下兩列array存成npz檔<br>
# array1 = np.array(range(30))<br>
# array2 = np.array([2,3,5])<br>
# 2. 讀取剛剛的npz檔，加入下列array一起存成新的npz檔
# 

# In[18]:


#. 將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])
with open ('test.npz', 'wb') as f:
    np.savez(f, array1, array2)
with open ('test.npz', 'wb') as f:
    a=np.load(f)
    b=np.load(f)
print (a)
print (b)


# In[9]:


#2. 讀取剛剛的npz檔，加入下列array一起存成新的npz檔
npzfile = np.load('test.npz')
print(npzfile['array1'])


# In[ ]:




