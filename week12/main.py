# Impordime klassi FailiLugeja teisest failist,
# mille ülesanne on lugeda andmeid CSV ja JSON failidest
from faili_lugemine import FailiLugeja

# Impordime ParooliHalduri klassi,
# mis tegeleb paroolide valideerimise, krüpteerimise ja salvestamisega
from paroolihaldur import ParooliHaldur

# Impordime Kasutaja klassi,
# mis tegeleb kasutajate registreerimise ja valideerimisega
from registreeri_kasutaja import Kasutaja


def main():
    # Loeme kasutajate andmed CSV failist
    andmed_csv = FailiLugeja.loe_csv_failist("kasutajad.csv")

    # Prindime kogu CSV sisu (debug / kontrollimiseks)
    print(andmed_csv)

    print("--- Kasutajad CSV failist ---")

    # Käime CSV-st saadud kasutajad ükshaaval läbi
    for i in andmed_csv:

        # Muudame ühe rea väärtused komaga eraldatud stringiks
        # (kasutatakse kasutaja objekti loomiseks)
        osad = ",".join(i.values())

        # Loome Kasutaja objekti CSV reast
        kasutaja_reg = Kasutaja.loo_csv_reast(osad)

        # Valideerime kasutajanime
        vastus_bool, vastus_str = kasutaja_reg.valideeri_kasutajanimi(i['kasutajanimi'])

        # Kui kasutajanimi ei ole korrektne, liigume järgmise juurde
        if vastus_bool == False:
            print(vastus_str)
            continue

        # Loome ParooliHaldur objekti selle kasutaja jaoks
        test = ParooliHaldur(i['kasutajanimi'])

        # Määrame parooli (käivitub setter: valideerimine + krüpteerimine)
        test.parool_hash = f"{i['parool']}"

        # Kuvame kasutaja täisnime ja vanuse
        print(f"{kasutaja_reg.taisnimi}, vanus: {kasutaja_reg.vanus}")


    # Loeme kasutajate andmed JSON failist
    andmed_json = FailiLugeja.loe_json_failist("kasutajad.json")

    print(f"\n\n--- Kasutajad CSV failist ---")

    # Käime JSON-ist saadud kasutajad ükshaaval läbi
    for i in andmed_json:

        # Loome Kasutaja objekti JSON objektist
        kasutaja_reg = Kasutaja.loo_json_objektist(i)

        # Valideerime kasutajanime
        vastus_bool, vastus_str = kasutaja_reg.valideeri_kasutajanimi(i['kasutajanimi'])

        # Kui kasutajanimi on vigane, jätame vahele
        if vastus_bool == False:
            print(vastus_str)
            continue

        # Loome ParooliHaldur objekti
        test = ParooliHaldur(i['kasutajanimi'])

        # Määrame parooli (setter kontrollib ja krüpteerib)
        test.parool_hash = f"{i['parool']}"

        # Kuvame kasutaja täisnime ja vanuse
        print(f"{kasutaja_reg.taisnimi}, vanus: {kasutaja_reg.vanus}")


    print(f"\n--- Salvestame paroolid ---")

    # Salvestame kõik paroolid JSON faili
    ParooliHaldur.salvesta_paroolid_faili()

    # Kuvame kasutajate statistika
    print(Kasutaja.kasutajate_statistika())

    # Kuvame registreeritud paroolide arvu
    print(f"Registreeritud paroole {ParooliHaldur.paroolide_arv()}")


# Käivitub ainult siis, kui seda faili käivitatakse otse
if __name__ == '__main__':
    main()
