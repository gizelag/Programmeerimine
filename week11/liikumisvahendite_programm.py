from liikumisvahend import Liikumisvahend
from laenutus import Laenutus

def lae_liikumisvahendi_andmed_failist(failinimi):
    try:
        with open(failinimi , "r", encoding="utf-8") as f:    #avame faili lugemiseks
            fail = f.readlines()  # loeme read listi

        for rida in fail:
            rida = rida.strip()
            if not rida:
                continue
            osad = [x.strip() for x in rida.split(";")]  #eradame sobiva eralldajaga


            if len(osad) != 4:  # Kui antud andmed ei ole õigete andmetega rida, jätame ta vahele
                print(f"Vahele jäetud vigane rida: {osad}")
                continue

            firma_nimi = osad[0]
            alustustasu = float(osad[1])
            saja_meetri_hind = float(osad[2])
            soidukaugus = float(osad[3])

            # Loome objektid
            lv = Liikumisvahend(firma_nimi, alustustasu, saja_meetri_hind, soidukaugus)

            liikumisvahendid.append(lv)
        return liikumisvahendid


    #veakontroll
    except FileNotFoundError as e:
        print(e)
        return []
    except Exception as e:
        print(e)
        return []



def main():
    # Kuvab kõik liikumisvahendid järjestatuna odavaimast kallimani:
    liikumisvahendid = lae_liikumisvahendi_andmed_failist(failinimi = "andmed_liikumisvahendid.txt")
    print(liikumisvahendid)
    if not liikumisvahendid:
        print(" Pole liikumisvahendeid seega lähen jala, programm lõppeb.")
        exit()
    laenutus = Laenutus(liikumisvahendid)
    laenutus.kuva_valik(5)

    # Naitame meetodite kasutamist
    laenutus.laenuta("Tuvi", 12)  # Laenutan 'Tuvi', sõidupikkus 12km

    laenutus.laenuta("Bolt", 3)  # Laenutan 'Bolt', sõidupikkus 3km

    laenutus.laenuta("Tuul", 18)  # Laenutan 'Tuul', sõidupikkus 18km

    laenutus.laenuta("Tuul", 5)  # Laenutan 'Tuul', sõidupikkus 5km

    laenutus.lae_liikumisvahendit("Tuul", 5)  # Laen liikumisvahendit 'Tuul', sõidupikkus 5km

    laenutus.laenuta("Tuul", 2)  # Laenutan 'Tuul', sõidupikkus 5km

    laenutus.laenuta("Tartu linnaratas", 30)  # Laenutan 'Tartu linnaratas', sõidupikkus 30km


if __name__ == "__main__":
    liikumisvahendid = []

    main()
