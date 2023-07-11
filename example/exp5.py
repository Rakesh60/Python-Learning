#prigram to find sum of all even and odd numbers upto user input
num=int(input('Enter a number'))


s_even=0
s_odd=0

count=1
while (count<=num):
    if (count%2==0):
       s_even=s_even+count
    else:
        s_odd=s_odd+count
    
    count+=1

print("Sum of even number is ",s_even)
print("Sum of odd number is ",s_odd)


# #Python program to calculate sum of odd and even numbers using while loop
# max=int(input("please enter the maximum value: "))
# even_Sum=0
# odd_Sum=0

# num=1
# while (num<=max):
#     if (num%2==0):
#         even_Sum=even_Sum+num
#     else:
#         odd_Sum=odd_Sum+num

#     num+=1

# print("The sum of Even numbers 1 to entered number", even_Sum)
# print("The sum of Even numbers 1 to entered number", odd_Sum)










































# num=int(input('Enter a number'))

# i=1
# even=odd=0
# while i<=num:
#     if (num%2)==0:
#         even=even+i
#     else:
#         odd=odd+i
#     i+=i

# print('Sum of even number is ',even)
# print('Sum of odd number is ',odd)

