#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd


# In[47]:


from sqlalchemy import create_engine


# In[48]:


# Connect to sqlite db


# In[49]:


db_file = r'salesdata.db'


# In[50]:


engine = create_engine(r"sqlite:///{}".format(db_file))


# In[81]:


sql = 'select * from scores'


# In[82]:


sales_data_df = pd.read_sql(sql, engine)


# In[83]:


sales_data_df


# In[ ]:




