#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd


# In[27]:


import numpy as np


# In[28]:


import glob


# In[29]:


call_data = pd.DataFrame()


# In[34]:


for f in glob.glob("weekly_call_data/week*.xlsx"): df = pd.read_excel(f); call_data = call_data.append(df,ignore_index=True)


# In[36]:


call_data.describe()


# In[ ]:




