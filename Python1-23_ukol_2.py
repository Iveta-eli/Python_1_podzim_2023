"""
Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. 
Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.  

Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník.
1)  Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit.
    Obě informace si ulož. Následně naprogramuj následující varianty:
2)  Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
3)  Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, 
    že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
4)  Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši,
    a sniž počet součástek na skladě o množství požadované zákazníkem.
"""

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

nazev = input("Zadej název součástky:")
mnozstvi = int(input("Zadej množství součástky:"))

print(nazev)
if nazev in sklad:
    print("Součástka je na skladě.")
    polozka = sklad.get(nazev)
    print(polozka)
    sklad[nazev] = polozka - mnozstvi

    if polozka - mnozstvi <= 1:
        print("Lze prodat pouze omezené množství kusů.")
        element = sklad.pop(nazev)
    else:
        print("Poptávku lze plně uspokojit.")

#polozka = sklad.get(nazev)
    print(polozka)
    print(sklad)
else:
    print("Součástka není skladem.")



