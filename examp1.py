n=int(input('Enter a number to check prime :'))
for i in range(2,n+1):         #i=2 , #i=3
    c=0                        #c=0 , c=1   
    for j in range(2,i//2+1):  #j=2-->(2//3)=0 ,#j=2-->1
        if(i%j==0):            #[2%2==0] TRUE, [3%2==0]
            c=c+1              #c=1
    if(c<=0):                  #c
        print(i,end=' ')