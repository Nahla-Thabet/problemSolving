n= int(input())
m= list(map(int, input().split()))
h=0
u=0
for i in m:
    h= h+i
    if(h<0):
        u=u+1
        h=0
print(u)
        
    
