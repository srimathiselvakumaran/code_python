s1,s2=map(int,input().split())
for i in range(s1+1,s2,1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i,end=" ")
