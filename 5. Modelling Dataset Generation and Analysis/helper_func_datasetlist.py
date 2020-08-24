# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 03:47:45 2019

@author: Gopalkrishnan
"""
import random
import os
import pandas as pd
activitydataSetsPath=r"C:\Users\Gopalkrishnan\Desktop\University at buffalo-Sem1\EAS 503-Python programming\Datasets"
def helper_func_datasetlist(dataSetsPath):
    import random
    import os
    import pandas as pd
    list1=[]
    directory = os.path.join(os.getcwd(),dataSetsPath)
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                filePath=dataSetsPath+"/"+file
                df= pd.read_csv(filePath)
                filename= file
                list1.append(filename)
                random.shuffle(list1)
                list2=list1[0:20]
                list3=list1[20:31]
    return list2,list3

helper_func_datasetlist(activitydataSetsPath)
