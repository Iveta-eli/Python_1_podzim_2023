# Úkol 6
class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne = True ):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne
       
    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            return "Potvrzuji zapůjče ní vozidla."
        else:
            return "Vozidlo není k dispozici."
    def get_info(self):
        return f"Registrační značka {self.registracni_znacka}, typ vozidla {self.typ_vozidla}."
       
auto1 = Auto("4A2 3020", "Peugeot 403 Cabria", 47534, True)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253, True)

znacka = input("Jakou značku chcete půjčit? Škoda nebo Peugot? :")
if znacka == "Peugot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif znacka == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
else:
    print("Vybrané vozidlo není k dispozici. Zvolte jinou značku.")

znacka = input("Jakou značku chcete půjčit? Škoda nebo Peugot? :")
if znacka == "Peugot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif znacka == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
else:
    print("Vybrané vozidlo není k dispozici. Zvolte jinou značku.")
