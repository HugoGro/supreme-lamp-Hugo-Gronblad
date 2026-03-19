#uppgift 8.1

#def area (a,b):
    #ar = a*a*3.14
    #cir = b*2*3.14
    #return ar,cir

#z = area(14,14)
#print(z)


#Uppgift 8.3

#def siffror (n):
    #mengd = 0
    #while n > 0:
        #n //= 10
        #mengd += 1
    #return mengd
#z = siffror(12321)
#print(z)

#Uppgift 8.4

#def fak (n):
    #resultat = 1

    #for i in range(1, n + 1):
        #resultat = resultat * i

    #return resultat



#tal = int(input("Ange ett heltal: "))
#var = fak(tal)

#print(f"Fakulteten av {tal} är {svar}")

#Uppgift 8.5

#def ar_perfekt (tal):
    #summa = 0


    #for i in range(1, tal):
        #if tal % i == 0:
            #summa += i


    #return summa == tal



#tal = int(input("Ange ett tal: "))

#if ar_perfekt(tal):
    #print(tal, "är ett perfekt tal")
#else:
    #print(tal, "är inte ett perfekt tal")

#Uppgift 8.6

#def med (sekvens):
    #summa = 0

    #for tal in sekvens:
        #summa += tal

    #eturn summa / len(sekvens)



#lista = [10, 20, 30, 40, 50]
#tupple = (1, 2, 3, 4, 5)


#print("Medelvärde för lista:", med (lista))
#print("Medelvärde för tuppel:", med(tupple))