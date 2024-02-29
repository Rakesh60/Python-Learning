import matplotlib.pyplot as plt
from matplotlib.figure import Figure
x=[10,20,30,40]
y=[20,25,35,55]
z=['AA','BB','CC','DD']
fig=plt.figure
plt.plot(x,y)
plt.title("Linear Graph",fontsize=35,color="Magenta")
plt.ylabel("Y-Axis hai bhai")
plt.xlabel("X-Axis label")
plt.ylim(0,90)
plt.xlim(0,100)
plt.xticks(x,labels=z)
plt.legend(["Linear Legend"])
plt.show()