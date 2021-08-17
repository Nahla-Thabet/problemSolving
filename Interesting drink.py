n=input()
price=[int(x)for x in input().split()]
q=input()
c=0
coins=[int(x)for x in input().split()]
for i in coins:
    for j in price:
        if coins[i]>=price[j]:
          c+=1

    print(c)

