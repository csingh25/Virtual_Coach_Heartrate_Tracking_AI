#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np

def helper_func_replace_missingval(activity,colName):
    indexNames = activity[ (activity[colName].isnull()) ].index.values.astype(int) 
    for i in indexNames:
        if(i != 0):
            activity.loc[i,colName]= activity.loc[i-1,colName] 
        else:
            activity.loc[i,colName]=  0
    return activity


# In[26]:


import pandas as pd
activityData=pd.read_csv('Running_09-55-32.csv')
activity=helper_func_replace_missingval(activityData,'elevation')
print(activity['elevation'])


# In[ ]:




