a,b=input().split()
a=str(bin(int(a)))[2:][::-1]
b=str(bin(int(b)))[2:][::-1]
c=1
f=0
for i,j in zip(a,b):
        if(i==j): c+=1
        if(i!=j): 
            print(c)
            f=1
            break
if(f==0):
    print(-1)
