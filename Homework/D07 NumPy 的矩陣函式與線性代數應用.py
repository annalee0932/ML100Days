#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# 作業目標<br>
# 活用矩陣運算，實做線性代數<br>
# 作業重點<br>
# 線性代數公式應用<br>
# 矩陣相乘維度需要對好，例如:2X3矩陣乘上3X5矩陣得到2X5矩陣

# 題目:<br>
# array1 = np.array([[10, 8], [3, 5]]) <br>
# 1. 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
# 2. 運用上列array計算特徵值、特徵向量?
# 3. 運用上列array計算SVD?

# In[1]:


import numpy as np


# In[2]:


#1. 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
array1 = np.array([[10, 8], [3, 5]])
transarray1=np.linalg.inv(array1)
np.matmul(array1, transarray1)


# In[5]:


#2. 運用上列array計算特徵值、特徵向量?
w,v=np.linalg.eig(array1)
print (w)
print (v)


# In[6]:


#3. 運用上列array計算SVD?
u,s,vh=np.linalg.svd(array1)
print (u)
print (s)
print (vh)


# In[ ]:




