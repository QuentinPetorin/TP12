def product(a,b):
    if (a or b) == 0:
        return 0
    elif (a or b) == 1:
        if a>b:
            return a
        else :
            return b

    else:
        return (a + (b-1)*a)








print(product(5,2)) # 10
print(product(9,3)) # 27
