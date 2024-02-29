import numpy as np
# l=[]
# for i in range(1,5):
#     x=int(input("Enter :"))
#     l.append(x)
    
# z=np.array(l)
# print(z.ndim)
# arr3=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
# print(arr3)
# print(arr3.ndim)
# print(arr3.flags)
#a=np.full((2,2), np.inf)
# print(type(np.inf))
# l=[1,2,3,4,5,6,7,8,9]
# a=np.asarray(l)
# print(type(a))
# print(a)
x=np.array([[10,20],[30,40]])
print("x:\n",x)
m=np.asmatrix(x)
print("m :\n",m)
x[0,0]=5
print("After changing m :\n",m)