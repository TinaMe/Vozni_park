
class Vozilo:
    def __init__(self, znamka, model, registracija, kilometri, servis):
        self.znamka = znamka
        self.model = model
        self.registracija = registracija
        self.kilometri = kilometri
        self.servis = servis

    def ime_vozila(self):
        return self.znamka + " " + self.model + " " + self.registracija

    def vozilo_vsi_podatki(self):
        return self.znamka + "|" + self.model + "|" + self.registracija + "|" + self.kilometri + "|" + self.servis

# -----> Ogled seznama vozil(voznega parka) <-----
def seznam_vozil(vozila):
    for index, vozilo in enumerate(vozila, 1):
        print "ID: " + str(index)
        print vozilo.ime_vozila()
        print vozilo.kilometri
        print vozilo.servis
        print "------------------------------"
    if not vozila:
        print "Na vasem seznamu ni nobenega vozila."

# -----> Dodajanje novega vozila <-----
def dodajanje_vozil(vozila):
    znamka = raw_input("Prosimo, vpisite znamko vozila: ")
    model = raw_input("Prosimo, vpisite model vozila: ")
    registracija = raw_input("Prosimo, vpisite registracijo vozila: ")
    kilometri = raw_input("Prosimo, vpisite stevilo prevozenih kilometrov vozila: ")
    servis = raw_input("Prosimo, vpisite datum zadnjega servisa vozila: ")

    new = Vozilo(znamka, model, registracija, kilometri, servis)
    vozila.append(new)

    print "------------------------------"
    print new.ime_vozila() + " je bilo uspesno dodano na seznam."

# -----> Urejanje stevila prevozenih kilometrov in datuma zadnjega servisa <-----
def urejanje_vozil(vozila):
    print "Izberite stevilko vozila, ki ga zelite urejati: "

    for index, vozilo in enumerate(vozila, 1):
        print str(index) + ") " + vozilo.ime_vozila()

    print "------------------------------"
    izbran_id = raw_input("Katero vozilo zelite urejati? (vpisite ID stevilko): ")
    izbrano_vozilo = vozila[int(izbran_id)]

    novi_kilometri = raw_input("Prosimo vpisite novo stevilo prevozenih kilometrov vozila " + izbrano_vozilo.ime_vozila() + " ")
    izbrano_vozilo.kilometri = novi_kilometri

    print "------------------------------"
    print "Kilometri so posodobljeni."

    novi_servis = raw_input("Prosimo vpisite nov datum opravljenega servisa vozila " + izbrano_vozilo.ime_vozila() + " ")
    izbrano_vozilo.servis = novi_servis

    print "------------------------------"
    print "Datum servisa je posodobljen."

# -----> Brisanje vozila s seznama <-----
def brisanje_vozila(vozila):
    print "Prosimo izbrite stevilko vozila, ki ga zelite izbrisati s seznama: "

    for index, vozilo in enumerate(vozila, 1):
        print str(index) + ") " + vozilo.ime_vozila()
        print "------------------------------"
        izbran_id = raw_input("Katero vozilo zelite izbrisati? (vpisite ID stevilko): ")
        izbrano_vozilo = vozila[int(izbran_id)]

        vozila.remove(izbrano_vozilo)
        print "------------------------------"
        print "Vozilo je bilo uspesno izbrisano s seznama."

# -----> Shrani vozila v obliki teksta <-----
def shrani_vozila(vozila):
    f = open("Vozni_park.txt", "w")
    for index, vozilo in enumerate(vozila, 1):
        f.write(vozilo.vozilo_vsi_podatki())
        f.write("\n")
    f.close()



def main():
    print "Dobrodosli v voznem parku!"

    audi = Vozilo(znamka="Audi", model="A4", registracija="LJ MV 729", kilometri="56821", servis="25.4.2016")
    volkswagen = Vozilo(znamka="Volkswagen", model="Passat", registracija="LJ KR 889", kilometri="47921", servis="12.6.2017")
    BMW = Vozilo(znamka="BMW", model="X5", registracija="LJ SR 846", kilometri="61321", servis="17.3.2016")

    vozni_park = [audi, volkswagen, BMW]

    while True:
        print "------------------------------"
        print "Prosimo, izberite eno izmed naslednjih moznosti: "
        print "a) Vpogled v celoten vozni park."
        print "b) Dodajanje novega vozila."
        print "c) Urejanje stevila prevozenih kilometrov ter datuma zadnjega servisa."
        print "d) Brisanje vozila s seznama."
        print "e) Shrani datoteko kot tekst."
        print "f) Izhod iz programa."
        print "------------------------------"

        izbira = raw_input("Vpisite katero moznost ste izbrali (a, b, c, d, e, f): ")
        print "------------------------------"

        if izbira.lower() == "a":
            seznam_vozil(vozni_park)
        elif izbira.lower() == "b":
            dodajanje_vozil(vozni_park)
        elif izbira.lower() == "c":
            urejanje_vozil(vozni_park)
        elif izbira.lower() == "d":
            brisanje_vozila(vozni_park)
        elif izbira.lower() == "e":
            shrani_vozila(vozni_park)
            print "Vozni park je zapisan v .txt datoteko."
        elif izbira.lower() == "f":
            print "Hvala in nasvidenje!"
            break
        else:
            print "Te izbire ni na seznamu. Prosimo vpisite se enkrat."
            continue


if __name__ == "__main__":
    main()