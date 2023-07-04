num1=int(input('Enter a number'))
num2=int(input('Enter a number'))
print('value of num1 and num 2 before',num1,num2)
#swap two variable without third variable
num1=num1+num2
num2=num1-num2
num1=num1-num2
print('value of num1 and num 2 After without temp',num1,num2)

#another method is 
num1,num2=num2,num1
print('value of num1 and num 2 After without temp',num1,num2)
