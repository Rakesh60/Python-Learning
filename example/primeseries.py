#Print Prime series upto user input
n=int(input('Enter th number for Prime series'))
for i in range(2,n+1):
    c=0
    # for j in range(2,i//2+1):
    j=2
    while(i2+1):
        if (i%j==0):
                c=c+1
        j=j+1
            
    if (c<=0):
        print(i,end=" ")