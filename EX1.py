def modulo(x, y) :

   if x/y == (1 or 0) :

       return x
   else :
       if x<y :
           y = y//x
           return modulo(x,y)
       else :
           x = x//y
           return modulo(x,y)




print(modulo(6, 13)) # 6
print(modulo(37, 10)) # 7
print(modulo(8, 2)) # 0
print(modulo(50, 7)) # 1
