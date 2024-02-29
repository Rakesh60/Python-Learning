import matplotlib.pyplot as plt
from matplotlib.figure import Figure
x= [10,20,30,40]
y= [20,25,35,55]
fig =plt.figure(figsize=(7,5), facecolor='g', edgecolor='b', linewidth=7)
ax = fig.add_axes([1,1,1,1])
ax.plot(x,y)
plt.title("Linear Graph", fontsize=25, color="yellow")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.ylim(0,80)
plt.xticks(x,label=["one", "two", "three", "four"])
plt.legend(["Legend No. 1"])
plt.show()