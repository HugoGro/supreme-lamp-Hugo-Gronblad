import temperatur

def inmatning():
    while True:
        print("\n Temperaturprogram")
        print("1. Rapportera temperatur")
        print("2. senaste temperatur")
        print("3. Avsluta")

        val = input("Välj alternativ ")

        if val == "1":
            try:
                tim = int(input("Ange timme (0-23): "))
                min = int(input("Ange minut (0-59): "))
                temp = float(input("Ange temperatur: "))

                if temperatur.observation(tim, min, temp):
                    print("sparad")
                else:
                    print("Felaktiga värden")

            except:
                print("Fel inmatning")

        elif val == "2":
            temp = temperatur.aktuell_temp()

            if temp is None:
                print("Ingen temperatur registrerad ännu.")
            else:
                print("Senaste temperatur:", temp)
                print("Tid:", temperatur.obs_tim(), ":", temperatur.obs_min())

        elif val == "3":
            print("Avslutar")
            break

        else:
            print("Ogiltigt val")


inmatning()