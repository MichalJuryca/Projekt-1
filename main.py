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
TEXTS = [
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

print("Vítejte v programu textový analyzátor, zadejte přihlašovací jmméno a heslo\n")
print("-" * 30) 
users = {"bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"}
zadane_jmeno = input("Zadejte jméno: ")
zadane_heslo = input("Zadejte heslo: ")

if zadane_jmeno in users and users[zadane_jmeno] == zadane_heslo:
    print("Přihlášení úspěšné!")
    # Zde může následovat kód pro případ úspěšného přihlášení
else:
    print("Neplatné jméno nebo heslo.")
    # Zde může následovat kód pro případ neúspěšného přihlášení













# uzivatele = {
#     "uzivatel1": "heslo1",
#     "uzivatel2": "heslo2",
#     "uzivatel3": "heslo3"
# }

# def over_uzivatele(zadane_jmeno, zadane_heslo):
#     if zadane_jmeno in uzivatele and uzivatele[zadane_jmeno] == zadane_heslo:
#         print("Přihlášení úspěšné!")
#         return True
#     else:
#         print("Neplatné jméno nebo heslo.")
#         return False

# # Testování
# zadane_jmeno = input("Zadejte uživatelské jméno: ")
# zadane_heslo = input("Zadejte heslo: ")

# if over_uzivatele(zadane_jmeno, zadane_heslo):
#     # Kód pro případ úspěšného přihlášení
#     print("Vítejte v aplikaci!")
# else:
#     # Kód pro případ neúspěšného přihlášení
#     print("Zkuste to znovu.")



