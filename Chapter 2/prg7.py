#Check Prime Number
num=int(input("Enter a number"))
fact=list()
for i in range(1,num+1):
   a= num//i
   if a*i==num:
       fact.append(i)
       
if(len(fact)>2):
    print('Not a prime number')
else:
    print('Prime number')