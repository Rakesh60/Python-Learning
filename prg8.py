import cmath
#Solve the Quadratic Equation
# ax^2+bx+c=0 a,b,c are real numbers and a!=0
a=float(input('Enter a: '))
b=float(input('Enter b: '))
c=float(input('Enter c: '))

#calculate the discriminant
d=(b**2)-(4*a*c)

#find the soluton
sol1=(-b-cmath.sqrt(d))/(2*a)  #-b+-SQRT(d/2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print('The Solutions are {0} and {1}'.format(sol1,sol2))