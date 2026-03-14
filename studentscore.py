import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data={'hours studied':[2,4,6,8,10,12,14,16,20,22],
     'hours slept':[1,2,3,4,5,6,7,8,9,10],
     'score':[10,20,30,40,50,60,70,80,90,100]
}
df=pd.dataframe(data)
print(df)
print(df.describe)
df.corr()
corr=df['hoursstudied'].corr(df['scores'])
corr=df['hoursslept'].corr(df['scores'])
m,b=np.polyfit(df['hours studied'],df['hoursslept'],df['scores'])
plt.scatter(df['hoursstudied'],df['hoursslept'],df['scores'],color='purple'
            label='actual data')
def predict-score():
Enter hoursstudied:
Enter hoursslept:


