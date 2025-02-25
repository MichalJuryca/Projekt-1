# Program bude obsahovat
# 1) vyžádání si od uživatele přihlašovací jméno a heslo
# 2) zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
# 3) pokud je registrovaný, pozdraví jej a umožní mu analyzovat texty
# 4) pokud není registrovaný, upozorní jej a ukončí program
# 5) registrovaní uživatelé
# user  password

# bob   123
# ann   pass123
# mike  password123
# liz   pass123

# 6) pokud uživatel vybere takové číslo textu, které není v zadání, 
#    program jej upozorní a skončí
# 7) pokud program zadá jiný vstup než číslo, program jej rovněž upozorní 
#    a skončí
# 8) statistiky - počet slov začínajících velkým písmenem
#               - počet slov psaných velkými písmeny
#               - počet slov psaných malými písmeny 
#               - počet čísel(ne cifer)
#               - sumu všech čísel(ne cifer) v textu

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Juryca
email: adruj@seznam.cz
"""
TEXTS = [  # datový typ list(multi line string se třemi jednoduchými uvozovkami. Je tedy již rozdělený.)
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
cara = "-" * 75  # Odstraněny závorky
print(cara)
print("Vítejte v programu textový analyzátor, zadejte přihlašovací jméno a heslo")
print(cara)
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
zadane_jmeno = input("Zadejte jméno: ")
zadane_heslo = input("Zadejte heslo: ")

if zadane_jmeno in users and users[zadane_jmeno] == zadane_heslo:
    print("Vítej v aplikaci, ", zadane_jmeno.capitalize(), "!")
    print(cara)
    cislo_vstup = input("Který odstavec ze 3 si přejete analyzovat? Zadejte číslo od 1 do 3.\n")
    print(cara)
    if cislo_vstup.isdigit():  # Kontrola, zda je vstup číselný
        cislo = int(cislo_vstup)
        if 1 <= cislo <= 3:
            vybrany_odstavec = TEXTS[cislo - 1]  # ověření počtu slov v odstavci
            pocet_slov = len(vybrany_odstavec.split())
            print("Ve vybraném textu je:           ", pocet_slov, "slov.")

            pocet_titlecase_slov = 0  # ověření Velké počáteční písmeno v odstavci
            for slovo in vybrany_odstavec.split():
                if slovo[0].isupper():
                    pocet_titlecase_slov += 1
            print("Z toho je:                      ", pocet_titlecase_slov, "slov s prvním velkým písmenem.")
            pocet_upercase_slov = 0  # ověření VELKÝCH slov v odstavci
            for slovo in vybrany_odstavec.split():
                if slovo.isupper() and slovo.isalpha():
                    pocet_upercase_slov += 1
            print("Z toho je:                      ", pocet_upercase_slov, "slov s velkými slovy.")
            pocet_lowercase_slov = 0  # ověření jen malých písmen
            for slovo in vybrany_odstavec.split():
                if slovo.islower():  # and slovo.isalpha(): #zatextováno, počítalo i číslice.
                    pocet_lowercase_slov += 1
            print("Z toho je:                      ", pocet_lowercase_slov, "slov s malými písmeny.")
            pocet_isdigit_cisel = 0  # ověření počtu cifer v odstavci
            for slovo in vybrany_odstavec.split():
                if slovo.isdigit():
                    pocet_isdigit_cisel += 1
                elif slovo == "US" and vybrany_odstavec.split()[
                    vybrany_odstavec.split().index(slovo) + 1] == "30":  # Tento řádek kódu kontroluje, zda je aktuální slovo "US" a zda je následující slovo "30". Pokud ano, znamená to, že se v textu nachází "US 30".
                    print("Z toho je:                      ", pocet_isdigit_cisel, "čísel.")
            slova = vybrany_odstavec.split()  # rozdělení odstavce a uložení do proměnné slova
            cisla = [int(slovo) for slovo in slova if
                     slovo.isdigit() and slovo != "30"]  # Comprenhenze zápis. Dále vynechání (nepravda != "30") do součtu všech čísel v odstavci.
            print(f"Z toho je:                    {sum(cisla)} součet čísel ve vybraném odstavci.")
            print(cara)

            cisty_odstavec = vybrany_odstavec.replace(',', '').replace('.', '').replace("US", "US").replace("30","_30")
                                                                                                                

            slova = cisty_odstavec.split()  # Rozdelenie textu na slova
            delky_slov = [len(slovo) for slovo in slova]

            kategorie = {}
            for delka in delky_slov:
                if delka not in kategorie:
                    kategorie[delka] = 0
                kategorie[delka] += 1

            print("\n| LEN |     OCCURENCES          | NR.")
            print(cara)
            for delka in sorted(kategorie.keys()):
                hvezdicky = '*' * kategorie[delka]
                print(f"| {delka:<3} | {hvezdicky:<20}    | {kategorie[delka]}")

        else:
            print("Neplatné číslo odstavce")
    else:
        print("Neplatný vstup. Zadejte prosím číslo")
else:
    print("neregistrovaný uživatel, ukončení programu..")


















