a=int(input("Enter 1st No "))
b=int(input("Enter 2nd No "))
def product(x,y):
    if x*y>=300:
        return x+y
print("The Sum of Two number if product of these {} and {} number is greater than 300 is ".format(a,b),product(a,b))