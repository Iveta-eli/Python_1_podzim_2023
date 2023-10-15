#Jednoduchá aplikace pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
"""
1) Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
2) Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

Tvůj program bude obsahovat dvě funkce:

První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420").
Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla.
Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu,
kterou vypíše uživateli.

Tipy:
    Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
    Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".
"""

def prvni_funkce():
    cislo = str(input("Napiš číslo, na které chceš odeslat svoji zprávu?"))
    delka_cisla = len(cislo)
    predvolba = str(cislo[0:4])

    if delka_cisla == 9 and predvolba != "+420":
         print("true")
         return True
    elif delka_cisla == 13:
        if predvolba == "+420":
            print("true")
            return True
        else:
            print("ERROR")
            return False
    else:
        print("ERROR")
        return False
    
def druha_funkce():
    text = input("Napiš text, který chceš odeslat:")
    print(len(text))
    delka_zpravy = len(text)
    zbytek = (delka_zpravy % 180)
    cena = (delka_zpravy // 180) * 3
    if zbytek > 0:
        cena = cena + 3
    print(cena,"Kč")
    return cena

if prvni_funkce():
    druha_funkce()

