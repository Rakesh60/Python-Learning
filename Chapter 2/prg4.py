num=int(input("Enter a number"))
fact=list()
sum=0
for i in range(1,num+1):
   a= num//i
   if a*i==num:
       fact.append(i)
       
for i in range(0,(len(fact)-1)):
    sum=sum+(fact[i])
if(sum>1):
    print("It is a perfect number :",sum)
print(fact)