#Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.
# 1) Soubor si ulož a načti do slovníku.
# 2) Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a).
#    Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů.
#    Pokud má méně než 60, hodnota bude "Fail".
# 3) Výsledný slovník ulož jako JSON do souboru prospech.json.


#Otevře json soubor:
import json
with open('body.json', encoding='utf-8') as file:
    body = json.load(file)

#Hlavní část kódu 
vysledky = {"jmeno": "hodnoceni"}

for keys, value in body.items():
    print(f"{keys}{value}")
    if value > 60:
        print("PASS")
        vysledky[keys]="pass"
    if value < 60:
        print("FAIL")
        vysledky[keys]="fail"#zapisuje do slovníku
print(body.keys)

import json
with open("prospech.json", mode="w", encoding="utf-8") as file_zapis:
   json.dump(vysledky, file_zapis, ensure_ascii=False) #ensure_ascii=false - zajistí mi český přepis
