#Print Fibonacci series
n=int(input('Enter a number :'))
n1=0
n2=1
for i in range(1,n):
    n3=n1+n2
    print(n3)
    n1,n2=n2,n3
    
    