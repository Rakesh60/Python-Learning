#find the armstrong number
n=int(input('Enter a number'))
sum=0
temp=n
while(n>0):
    r=n%10 #find the last digit 
    sum=sum+r**3
    n=n//10 #it helps breaking the larger digit
if(sum==temp):
    print('This is a Armstrong Number')
else:
    print('Not Armstrong')      