import pandas as pd
import matplotlib.pyplot as plt

names= ['virat', 'mohit', 'keerti', 'sunny','pooja']
dob=[12,20,26,17,11]
surname= ['sharma', 'mourya', 'viswakarma','chauhan','singh']

1
nameSeries=pd.Series(names)
dobSeries=pd.Series(dob)
frame={'NAME':nameSeries,'D-O-B':dobSeries}
result=pd.DataFrame(frame)
result['SURNAME']=pd.Series(surname)
print(result)
result.plot.bar(x='names')
plt.show()



#print (nameSeries)
