def ar_perfekt (tal):
    summa = 0


    for i in range(1, tal):
        if tal % i == 0:
            summa += i


    return summa == tal



tal = int(input("Ange ett tal: "))

if ar_perfekt(tal):
    print(tal, "är ett perfekt tal")
else:
    print(tal, "är inte ett perfekt tal")