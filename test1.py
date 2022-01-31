#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
import pandas as pd
food_df = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding="ISO-8859-1")
food_df.describe(include='all')


# In[40]:


food_df.head(10)


# In[83]:


food_df.groupby('Element')['Y2014'].sum()


# In[84]:


food_df.groupby('Element')['Y2018'].sum()


# In[85]:


food_df['Area'].unique().size


# In[ ]:





# In[119]:


#Question 11
food_df.groupby('Item')['Y2014'].sum()
food_df.groupby('Item')['Y2017'].sum()


# In[122]:


#Question 12
food_df['Y2015'].mean()
food_df['Y2015'].std()


# In[130]:


#question 13
food_df['Y2016'].isnull().sum()
(food_df['Y2016'].isnull().sum()/food_df['Y2016'].notnull().sum())*100


# In[134]:


#question 15 and 16
food_df.groupby('Element').sum()


# In[137]:


#question 17 and 18
food_df.groupby('Element')['Y2018'].sum()


# In[ ]:


#Question 20
food_df['Area'].unique().size

