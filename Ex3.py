def pow(x,n):

    if n == 0 :
        return 1

    elif n == 1 :
        return x

    else :
        n = n-1

        if n == 1:
            return x*x
        else :
            return x**(n+1)










print(pow(42, 0)) # 1
print(pow(1, 10)) # 1
print(pow(7, 2)) # 49
print(pow(2, 5)) # 32

