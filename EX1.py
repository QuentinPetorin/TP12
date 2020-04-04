def modulo(x, y) :

   if y==0 :
       return x
   else :
       x*=x
       return y*modulo(x,y)



print(modulo(6, 13)) # 6
print(modulo(37, 10)) # 7
print(modulo(8, 2)) # 0
print(modulo(50, 7)) # 1
