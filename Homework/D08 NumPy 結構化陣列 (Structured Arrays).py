#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# 作業目標<br>
# 在一個陣列中放入多屬性陣列，進一步對陣列做運算<br>
# 作業重點<br>
# 在建立結構化陣列前需要先設定屬性，在做運算時須注意資料屬性

# 題目:<br>
# name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']<br>
# sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']<br>
# weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]<br>
# rank_list = [8,1,5,4,7,6,2,3]<br>
# myopia_list = [True,True,False,False,True,True,False,False]<br>
# 1. 將上列list依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]<br>
# 2. 呈上題，將array中體重(weight)數據集取出算出全部平均體重
# 3. 呈上題，進一步算出男生(sex欄位是boy)平均體重、女生(sex欄位是girl)平均體重
# 

# In[1]:


import numpy as np 


# In[11]:


name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]


# In[38]:


#1. 將上列list依['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
array1=np.array(name_list+sex_list+weight_list+rank_list+myopia_list)
array2=array1.reshape((8,5),order='F')
array2


# In[ ]:


#2. 呈上題，將array中體重(weight)數據集取出算出全部平均體重


# In[ ]:


#3. 呈上題，進一步算出男生(sex欄位是boy)平均體重


# In[ ]:


#3. 呈上題，進一步算出女生(sex欄位是girl)平均體重


# In[ ]:




