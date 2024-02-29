import matplotlib. pyplot as plt
import pandas as pd
data= pd.read_csv( 'tips.csv')
x=data['day']
y=data['total_bill']
plt.bar(x,y)
plt.title("Tips Dataset")
plt.ylabel("Total Bill")
plt. xlabel("Day")
plt. show()