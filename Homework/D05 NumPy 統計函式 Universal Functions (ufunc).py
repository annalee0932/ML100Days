#!/usr/bin/env python
# coding: utf-8

# 作業目標<br>
# 計算有缺失值的資料，統計量實作<br>
# 作業重點<br>
# 當遇到缺失值有函式可以處理，不須額外寫程式刪除<br>
# 計算統計量時不能出現缺失值

# 題目:<br>
# english_score = np.array([55,89,76,65,48,70])<br>
# math_score = np.array([60,85,60,68,np.nan,60])<br>
# chinese_score = np.array([65,90,82,72,66,77])<br>
# 上3列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文55分、數學60分、國文65分，今天第五位同學因某原因沒來考試，導致數學成績缺值，運用上列數據回答下列問題。<br>
# 1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
# 2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
# 3. 用補考後資料找出與國文成績相關係數最高的學科?

# In[2]:


import numpy as np


# In[3]:


english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])


# In[35]:


#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
english=[np.mean(english_score), np.amax(english_score), np.amin(english_score), np.std(english_score)]
print (english)
math=[np.nanmean(math_score), np.nanmax(math_score), np.nanmin(math_score), np.nanstd(math_score)]
print (math)
chinese=[np.mean(chinese_score), np.amax(chinese_score), np.amin(chinese_score), np.std(chinese_score)]
print (chinese)


# In[46]:


#2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
math_score[5]=55
math=[np.nanmean(math_score), np.nanmax(math_score), np.nanmin(math_score), np.nanstd(math_score)]
print (math)


# In[5]:


#3. 用補考後資料找出與國文成績相關係數最高的學科?


# In[59]:


english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
englishtochinese_corr=np.correlate(english_score, chinese_score)
mathtochinese_corr=np.correlate(math_score, chinese_score)
if englishtochinese_corr >=mathtochinese_corr:
    print ('與國文成績相關係數最高的學科是英文')
else:
    print ('與國文成績相關係數最高的學科是數學')


# In[ ]:




