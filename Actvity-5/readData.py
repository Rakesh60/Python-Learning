import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Datasheet.csv')
df["Profit/Loss"].plot.bar()
plt.show()

print(df) 