def area(a):
    ar = a * a * 3.14
    cir = a * 2 * 3.14

    if a <= 0:
        print('radien är inte positiv')
    else:
        print(ar,cir)
    return ar,cir
z = area(0)
print(z)













