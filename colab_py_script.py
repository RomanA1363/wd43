# list working directory?
!pwd
# makes directory
!mkdir roman
# basic loop
for i in range (6):
    print (i)
# starts here:
# import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('display.max_columns' , 200)
df = pd.read_csv('/CoLab-Dataset-1-100K.csv')
df.shape
df.head()
df.columns
df.dtypes
df.describe()
df.isna().sum()
df.duplicated()
df.loc[df.duplicated()]
df.query('last_name == "Mumbey"')

