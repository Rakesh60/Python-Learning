import ctypes
a=5
b=2
print('Address at',id(a),'Before Swapping A=',a)
print('Address at',id(b),'Before Swapping B=',b)
addOfa=id(a)
addOfb=id(b)


a=a+b
b=a-b
a=a-b

print('\n\nAddress at',id(a),'After Swapping A=',a)
print('Address at',id(b),'After Swapping B=',b)
addOfa=id(a)
addOfb=id(b)
