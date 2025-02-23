ukoly = []

def pridat_ukol():
    ukol = input("Zadejte novy ukol.")
    ukoly.append(ukol)
    print(f"Nový úkol {ukol} byl přidán.")

def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů.\n")
    else:
        print("Seznam ukolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol}")
        print()

def odstranit_ukol():
    zobrazit_ukoly()
    if ukoly:
        try:
            cislo = int(input("Zadejte číslo úkolu k odstranění: "))
            if 1 <= cislo <= len(ukoly):
                odebranej_ukol = ukoly.pop(cislo - 1)
                print(f"Úkol {odebranej_ukol} byl odstraněň.\n")
            else:
                print("Neplatné číslo úkolu. Zkuste to znovu.\n")
        except ValueError:
            print("Nepltný vstup! Zadejte číslo úkolu.\n")

def hlavni_menu():
    while True:
        print("SPRÁVA ÚKOLŮ - HLAVNÍ MENU ")
        print("1) Přidat úkol.")
        print("2) Zobrazit všechny úkoly.")
        print("3) Odstranit úkol.")
        print("4) Konec")

        volba = input("Vyberte možnost (1 - 4): ")
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu!")
            break
        else: 
            print("Neplatná volba zkuste to znovu!\n")
hlavni_menu()