

def kontrolli_temperatuur(temperature):
    if 36.0 <= temperature <= 37.5:
        return "norm"
    elif (35.5 <= temperature <= 35.9) or (37.6 <= temperature <= 38.0):
        return "piiripealne"
    else:
        return "kõrvalekalle"

def kontrolli_vererohk(blood_pressure):
    if 100 <= blood_pressure <= 129:
        return "norm"
    elif (90 <= blood_pressure <= 99) or (130 <= blood_pressure <= 139):
        return "piiripealne"
    else:
        return "kõrvalekalle"


def kontrolli_pulss(BPM):
    if 60 <= BPM <= 100:
        return "norm"
    elif (50 <= BPM <= 100) or (101 <= BPM <= 110):
        return "piiripealne"
    else:
        return "kõrvalekalle"

def main():
    temperature = float(input("Sisesta kehatemperatuur (): "))
    temp_staatus = kontrolli_temperatuur(temperature)
    print(f"Temperatuur: {temp_staatus}")
    blood_pressure = int(input("Sisesta vererõhk (mmHg): "))
    bloodpressure_staatus = kontrolli_vererohk(blood_pressure)
    print(f"Vererõhk: {bloodpressure_staatus}")

    BPM = int(input("Sisesta pulss (BPM): "))
    BPM_staatus = kontrolli_pulss(BPM)
    print(f"Pulss: {BPM_staatus}")
    halb_tunne = input("Kas patsient tunneb end halvasti? (jah/ei): ").strip().lower()
    staatused = [temp_staatus, bloodpressure_staatus, BPM_staatus]
    kõrvalekaldeid = staatused.count("kõrvalekalle")
    piiripealseid = staatused.count("piiripealne")

    print(f"KOKKUVÕTE: {kõrvalekaldeid} kõrvalekalle, {piiripealseid} piiripealne")


    if kõrvalekaldeid >= 2:
        soovitus = "Pöördu arsti poole."
    elif halb_tunne == "jah" and (kõrvalekaldeid >= 1 or piiripealseid >= 1):
        soovitus = "Pöördu arsti poole."
    elif kõrvalekaldeid == 0 and piiripealseid > 0:
        soovitus = "Jälgi oma tervist."
    elif kõrvalekaldeid == 0 and piiripealseid  == 0:
        soovitus = "Tervislik seisund on hea."
    else:
        soovitus = "Pöördu arsti poole."#kui patsient tunneb end hasti aga on korvalekaldeid
    print(f"Soovitus: {soovitus}")

if __name__ == "__main__":
    main()



