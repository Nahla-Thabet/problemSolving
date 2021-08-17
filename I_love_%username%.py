'''n=int(input())
m=list(map(int,input().split()))

output=0
minn= m[0]
maxx=m[0]

for i in range(n):
    if m[i] > maxx:
            #or m[i]< minn:
        output +=1
    if m[i]< minn:
        output += 1
print(output)'''
input()
count=0
x=list(map(int,input().split()))
for i in range(1,len(x)):
    if(x[i]<min(x[0:i]) or x[i]>max(x[0:i])):
        count+=1
print(count)