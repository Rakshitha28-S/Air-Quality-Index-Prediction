#!/usr/bin/env python
# coding: utf-8

# # AQI Prediction Model using Python

# - PM2.5 PM10
# - NO, No2
# - NH3-Ammonia
# - CO
# - So2
# - o3
# - Benzene, Toluene, Xylene

# In[3]:


pip install numpy pandas matplotlib seaborn scikit-learn


# In[6]:


# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
filterwarnings('ignore')


# In[7]:


df = pd.read_csv('air quality data.csv')
df.head() #top 5 rows


# In[9]:


# Shape - rows and cols!
df.shape


# In[10]:


# information
df.info()


# In[11]:


# to know duplicate values
df.duplicated()


# In[12]:


# to know duplicate values
df.duplicated().sum()


# In[13]:


# to Check missing values
df.isnull()


# In[14]:


# to Check missing values
df.isnull().sum()


# In[15]:


# Drop the rows where 'AQI' has missing values
df.dropna(subset=['AQI'], inplace = True)


# In[16]:


df.isnull().sum().sort_values(ascending=False)


# In[17]:


df.shape


# In[19]:


# summary of statistics dataset
df.describe()


# In[25]:


# percentage of the null values
null_values_percentage = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending=False)
null_values_percentage


# In[ ]:




