import matplotlib.pyplot as plt 
import pandas as pd
cars=['Audi','BMW',"FORD",'Tesla','Jaguar']
data=[23,10,35,15,12]
#data=pd.read_csv('tips.csv')
plt.pie(data,labels=cars)
plt.title("Car Data")
plt.show()
1