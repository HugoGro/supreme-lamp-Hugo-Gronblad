import ssp

def spela():
    print("=== Sten, Sax, Påse ===")

    while True:
        input("Clicka på enter nr 1")
        drag1 = ssp.sspp()
        print("Spelare 1 fick:", drag1)

        input("Spelare 2, tryck Enter för att få ditt drag...")
        drag2 = ssp.sspp()
        print("Spelare 2 fick:", drag2)

        resultat = ssp.vinnare(drag1, drag2)
        print("Resultat:", resultat)

        # Fråga om man vill spela igen
        igen = input("\nVill ni spela igen? (j/n): ").lower()

        if igen != "j":
            print("Tack för att ni spelade!")
            break

        print("\n------------------------\n")



spela()
