def listSum(l1,l2=[]):
   # i = l1[0]
    if len(l1) == 0:
        return 0
    else :
       l2.append(l1[-1])
       sum = l2[-1:]

       l1.remove(l1[len(l1)-1])

       listSum(l1,l2)
       return sum










print(listSum([])) # 0
#print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11


