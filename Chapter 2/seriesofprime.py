#Print Prime series upto user input
n=int(input('Enter th number for Prime series'))
for i in range(2,n+1):
    
    c=0
    
    for j in range(2,i//2+1):
        if (i%j==0):
            c=c+1
   
    if (c<=0):
        print('value of c\n',c)
        print(i,end=" ")