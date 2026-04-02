import ssp

def spel ():
    print(" Sten, Sax, Påse?")

    while True:
        input("clicka på enter")
        nr1 = ssp.sspp()
        print("Spelare 1 fick:", nr1)

        input("clicka på enter igen")
        nr2 = ssp.sspp()
        print("Spelare 2 fick:", nr2)

        resultat = ssp.vinnare(nr1, nr2)
        print("Vinnare:", resultat)


        igen = input("\nVill ni spela igen? (j/n): ").lower()

        if igen != "ja":
            break

        print("\n------------------------\n")



spel()
