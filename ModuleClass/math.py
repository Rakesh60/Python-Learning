x=int(input('Enter first number '))
y=int(input('Enter Second number '))
z=input('Enter z ')

def maths(x,y,z):
    if(z == '+'):
        return x + y
    # Substraction (-)
    elif(z == '-'):
        return x - y
    # Multiplication (*)
    elif(z == '*'):
        return x * y
    # Division (/)
    elif(z == '/'):
        return x / y
    # Modulo (%)
    elif(z == '%'):
        return x % y
    # Unknown
    else:
        return 'Sorry, but I cannot understand your operation'
    
    
print(maths(x,y,z))
    
