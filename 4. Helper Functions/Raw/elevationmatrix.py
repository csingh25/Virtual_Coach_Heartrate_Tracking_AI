#!/usr/bin/env python
# coding: utf-8

# In[10]:


#activityData=pd.read_csv('Running_09-55-32.csv')

import pandas as pd
import numpy as np

def helper_func_Elevation(activity):
    for n in range(10,191,10):
        # computing a rolling change in elevation over past n seconds
        change_elevation=activityData['elevation'].rolling(window=n).apply(lambda activityData: activityData[n-1] - activityData[0])
        actual_elevation=activity.loc[:,'elevation']
        # if the past n seconds are not available, replace the metric with the current value
        treated_elevation = change_elevation.combine_first(actual_elevation)
        name = 'elevation_' + str(n)
        treated_elevation=treated_elevation.rename(name)
        activity = pd.concat([activity, treated_elevation], axis=1)
    return(activity)


# In[11]:


import pandas as pd
activityData=pd.read_csv('Running_09-55-32.csv')
activity=helper_func_Elevation(activityData)
print(activity['elevation_10'])


# In[ ]:




