'''alist=[10, 13, 51, 6, 9, 45, 35, 22, 90]    #Bubble Sor@@@
def smartbubblesort(alist):
    n=len(alist)
    exchange=True
    for passnum in range (n-1, 0 , -1):
        if exchange == False :
            break
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i] ,alist[i+1] = alist[i+1] , alist[i]
                exchange = True
    return alist
print(smartbubblesort(alist)) 
#********************************************************************** '''

'''def selectionsort (alist):
    n=len(alist)
    for i in range (n-1):
        min =alist[i]
        minposition = i
        for j in range (i+1, n):
            if alist[j] < min :
             min = alist[j]
             minposition =j
        alist[i], alist[minposition] = alist[minposition], alist[i]
    return alist

print(selectionsort(alist))

***********************************************'''
