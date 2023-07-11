#Factor of Number
num=int(input("Enter a number"))
fact=list()
for i in range(1,num+1):
   a= num//i
   if a*i==num:
       fact.append(i)
       
print(fact)