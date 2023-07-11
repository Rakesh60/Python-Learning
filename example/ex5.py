year=int(input('Enter a year'))

if year%400==0:
    if year%100==0:
        if year%4==0:
            print("Its a leap Year")
        else:
            print('Not a leap Year')
    else:
        print('No a leap Year')
else:
    print('No a leap year')