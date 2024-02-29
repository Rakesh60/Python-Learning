import numpy as np
ls=[5,6]
var=np.array([1,2,3,4,7,8])
x=np.searchsorted(var,ls)
for i in range(len(ls)):
    z=ls[i]
    print(z)
    var[x+i]=z
   
    
print(var)