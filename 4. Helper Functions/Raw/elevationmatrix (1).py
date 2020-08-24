#!/usr/bin/env python
# coding: utf-8

# In[13]:


#activityData=pd.read_csv('Running_09-55-32.csv')

import pandas as pd
import numpy as np

def helper_func_Elevation(activity):
    for n in range(10,191,10):
        # computing a rolling change in elevation over past n seconds
        change_elevation=activity['elevation'].rolling(window=n).apply(lambda activity: activity[n-1] - activity[0])
        actual_elevation=activity.loc[:,'elevation']
        # if the past n seconds are not available, replace the metric with the 0 value as it is nearest to any moment change
        # in the elevation
        change_elevation[0:n]=0
        name = 'elevation_' + str(n)
        treated_elevation=change_elevation.rename(name)
        activity = pd.concat([activity, treated_elevation], axis=1)
    return(activity)


# In[14]:


import pandas as pd
activityData=pd.read_csv('Running_08-12-06.csv')
#print(activityData[100,'distance'])
activity=helper_func_Elevation(activityData)
print(activity['elevation_20'])


# In[ ]:




