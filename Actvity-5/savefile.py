import matplotlib.pyplot as plt
year=['2010','2004','2008','2022','2023']
production=[25,15,35,30,10]
plt.bar(year,production)
plt.savefig('output.jpg')
plt.savefig("output1",facecolor='y',bbox_inches='tight',pad_inches=0.3,transparent=True)