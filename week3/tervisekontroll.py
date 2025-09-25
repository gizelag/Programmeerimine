

def kontrolli_temperatuur(temperature):
    if 36.0 <= temperature <= 37.5:
        return "norm"
    elif (35.5 <= temperature <= 35.9) or (37.6 <= temperature <= 38.0):
        return "piiripealne"
    else:
        return "kõrvalekalle"

def kontrolli_vererõhk(blood_pressure):
    if 100 <= blood_pressure <= 129:
        return "norm"
    elif (90 <= blood_pressure <= 99) or (130 <= blood_pressure <= 139):
        return "piiripealne"
    else:
        return "kõrvalekalle"


def kontrolli_pulss(bpm):
    if 60 <= bpm <= 100:
        return "norm"
    elif (50 <= bpm <= 100) or (101 <= bpm <= 110):
        return "piiripealne"
    else:
        return "kõrvalekalle"

def main():
    temperature = float(input("Sisesta kehatemperatuur (): "))
    temp_staatus = kontrolli_temperatuur(temperature)
    print(f"Temperatuur: {temp_staatus}")
    blood_pressure = int(input("Sisesta vererõhk (mmHg): "))
    bloodpressure_staatus = kontrolli_vererõhk(blood_pressure)
    print(f"Vererõhk: {bloodpressure_staatus}")

    bpm = int(input("Sisesta pulss (bpm): "))
    bpm_staatus = kontrolli_pulss(bpm)
    print(f"Pulss: {bpm_staatus}")
    halb_tunne = input("Kas patsient tunneb end halvasti? (jah/ei): ").strip().lower()
    staatused = [temp_staatus, bloodpressure_staatus, bpm_staatus]
    korvalekaldeid = staatused.count("kõrvalekalle")
    piiripealseid = staatused.count("piiripealne")

    print(f"KOKKUVÕTE: {korvalekaldeid} kõrvalekalle, {piiripealseid} piiripealne")


    if korvalekaldeid >= 2:
        soovitus = "Pöördu arsti poole."
    elif halb_tunne == "jah" and (korvalekaldeid >= 1 or piiripealseid >= 1):
        soovitus = "Pöördu arsti poole."
    elif korvalekaldeid == 0 and piiripealseid > 0:
        soovitus = "Jälgi oma tervist."
    elif korvalekaldeid == 0 and piiripealseid  == 0:
        soovitus = "Tervislik seisund on hea."
    else:
        soovitus = "Pöördu arsti poole."#kui patsient tunneb end hasti aga on korvalekaldeid
    print(f"Soovitus: {soovitus}")

if __name__ == "__main__":
    main()



