import pandas as pd
import numpy as np
heart_rate=pd.read_csv('Running_09-55-32.csv')
heart_rate.describe
heart_rate.info()
corr=heart_rate.corr()
