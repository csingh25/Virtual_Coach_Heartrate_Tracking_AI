#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Changing the working directory to the location where the activity datasets are present
get_ipython().run_line_magic('cd', '"C:\\UB\\Studies\\Semester 1\\Programming\\virtual_coach\\2. Activity Datasets"')


# In[2]:


import pandas as pd
import numpy as np


# In[73]:


# This function accepts a pandas dataframe, adds the custom hearrate metrics to it and returns a pandas dataframe 
# activity=pd.read_csv('Running_09-55-32.csv')

import pandas as pd
import numpy as np
def helper_func_heartrate(activity):
    for n in range(10,381,10):
        # computing a rolling average of heartrate over past n seconds
        avg_hr=activity.loc[:,'heartRate'].rolling(window=n).mean()
        actual_hr=activity.loc[:,'heartRate']
        # if the past n seconds are not available, replace the metric with the current value
        treated_hr = avg_hr.combine_first(actual_hr)
        name = 'heartRate_' + str(n)
        treated_hr=treated_hr.rename(name)
        activity = pd.concat([activity, treated_hr], axis=1)
    return(activity)


# In[74]:


def helper_func_speed(heart_rate):
    for n in range(10,361,10):
        #print(n)
        distance_covered=heart_rate['distance']-heart_rate['distance'].shift(n)
        speed=distance_covered/n
        avg_speed=heart_rate['distance']/(heart_rate['time']+1)
        treated_speed = speed.combine_first(avg_speed)
        name = 'speed_' + str(n)
        treated_speed=treated_speed.rename(name)
        heart_rate = pd.concat([heart_rate, treated_speed], axis=1)
    return(heart_rate)


# In[87]:


#Testing for a sample dataset

activity=pd.read_csv('Running_10-51-40.csv')
activity=helper_func_heartrate(activity)
activity=helper_func_speed(activity)


# In[119]:


# fitting a sample linear model

s=120

activity=pd.read_csv('Running_19-30-16.csv')

activity=helper_func_heartrate(activity)
activity=helper_func_speed(activity)

heart_rate_future=activity['heartRate'].shift(-s)
activity.drop(activity.tail(s).index,inplace=True)
heart_rate_future.drop(heart_rate_future.tail(s).index,inplace=True)

from sklearn.linear_model import LinearRegression

reg = LinearRegression().fit(activity, heart_rate_future)
pred = reg.predict(np.array(activity))

from sklearn.metrics import r2_score
y_true = heart_rate_future
y_pred = pred
r2_score(y_true, y_pred)  


# In[ ]:


activity['Zone_Level'] = 0
activity.loc[activity.heartRate >= 180,'Zone_Level'] = 1


# In[120]:


# out of sample validation 
# God is with us 
activity=pd.read_csv('Running_07-10-59.csv')
activity=helper_func_heartrate(activity)
activity=helper_func_speed(activity)

heart_rate_future=activity['heartRate'].shift(-s)

activity.drop(activity.tail(s).index,inplace=True)
heart_rate_future.drop(heart_rate_future.tail(s).index,inplace=True)

pred=reg.predict(np.array(activity))

from sklearn.metrics import r2_score
y_true = heart_rate_future
y_pred = pred
r2_score(y_true, y_pred)  


# In[72]:


from pandas import DataFrame

Numbers = {'set_of_numbers': [1,2,3,4,5,6,7,8,9,10]}
df = DataFrame(Numbers,columns=['set_of_numbers'])

df['equal_or_lower_than_4?'] = df['set_of_numbers'].apply(lambda x: 'True' if x <= 4 else 'False')

print (df)


# In[82]:


activity


# In[ ]:




