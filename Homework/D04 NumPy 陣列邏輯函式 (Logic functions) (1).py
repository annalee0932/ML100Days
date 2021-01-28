#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# 作業目標<br>
# 熟悉邏輯運算<br>
# 作業重點<br>
# 五大類邏輯函式與其對應的函式操作

# 題目:<br>
# english_score = np.array([55,89,76,65,48,70])<br>
# math_score = np.array([60,85,60,68,55,60])<br>
# chinese_score = np.array([65,90,82,72,66,77])<br>
# 上3列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文55分、數學60分、國文65分，運用上列數據回答下列問題。<br>
# 1. 有多少學生英文成績比數學成績高?
# 2. 是否全班同學最高分都是國文?
# 
# 
# 

# In[1]:


import numpy as np


# In[26]:


#1.有多少學生英文成績比數學成績高?
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
goodenglish=np.array(english_score>math_score)
np.sum(goodenglish)


# #2.是否全班同學最高分都是國文?
# badenglish=np.array(chinese_score>english_score)
# badmath=np.array(chinese_score>math_score)
# np.logical_and(badenglish, badmath)
# np.logical_and((badenglish, badmath).any())
# 

# In[29]:


#2.是否全班同學最高分都是國文? 
badenglish=np.array(chinese_score>english_score) 
badmath=np.array(chinese_score>math_score) 
print(np.logical_and(badenglish, badmath))
np.logical_and(badenglish, badmath).any()


# In[ ]:




