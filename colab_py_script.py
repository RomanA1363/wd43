#/content/drive/MyDrive/CoLabData/combined.csv
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('display.max_columns' , 200)
df = pd.read_csv('/content/drive/MyDrive/CoLabData/combined.csv')
df.shape


