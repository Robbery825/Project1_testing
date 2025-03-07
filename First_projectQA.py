ukoly = []

def pridat_ukol():
    while True:
        ukol = input("Zadejte nový úkol: ").strip()  
        if ukol:  
            ukoly.append(ukol)  
            print(f"{len(ukoly)}) Nový úkol \"{ukol}\" byl přidán.\n") 
            break  
        else:  
            print("Název úkolu, nemůže být prázdný.")

def zobrazit_ukoly():
    print(f"Seznam úkolů (počet úkolů: {len(ukoly)}):")  
    if not ukoly:
        print("Seznam úkolů je prázdný.\n")  
    else:
        print("Seznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol}")
        print()

def odstranit_ukol():
    if not ukoly:
        print("Seznam je prázdný. Není co odstranit.\n")  
        return
    zobrazit_ukoly()

    while True:
        cislo = input("Zadejte číslo úkolu k odstranění: ").strip()  

        if not cislo: 
            print("Chyba: Vstup nemůže být prázdný!")
            continue

        if not cislo.isdigit(): 
            print("Neplatný vstup! Zadejte číslo úkolu.")
            continue

        cislo = int(cislo)  
        
        if 1 <= cislo <= len(ukoly):
            odebrany_ukol = ukoly.pop(cislo - 1)
            print(f"Úkol \"{odebrany_ukol}\" byl odstraněn.\n")
            break
        else:
            print(f"Neplatné číslo úkolu. Zadejte číslo v rozsahu 1 - {len(ukoly)}.")

def hlavni_menu():
    while True:
        print("\nSPRÁVA ÚKOLŮ - HLAVNÍ MENU")
        print("1) Přidat úkol")
        print("2) Zobrazit všechny úkoly")
        print("3) Odstranit úkol")
        print("4) Konec")

        volba = input("Vyberte možnost (1 - 4): ").strip()
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
            print("Neplatná volba, zkuste to znovu!\n")

if __name__ == "__main__":
    hlavni_menu()
