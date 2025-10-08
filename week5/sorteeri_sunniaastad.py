from andmete_lugeja import loe_tekst_failist
def lae_koik_sunniaastad_failist(failinimi):
    andmed = loe_tekst_failist(failinimi)
    sunniaastad = []
    print(f"Loen sünniaastate andmeid failist {failinimi}")
    if andmed is None:
        print("Viga: failist ei saanud andmeid lugeda.")
        return []
    kokku = 0
    try:
        #sunniaastad = [int(rida.strip()) for rida in andmed.splitlines() if rida.strip()]
        for rida in andmed.splitlines():
            rida = rida.strip()
            if not rida:
                continue
            try:
                aasta= int(rida)
                sunniaastad.append(aasta)
                kokku += 1
            except ValueError:
                continue

    except Exception as e:
        print(e)
    print(f"Kokku leitud {kokku} numbrilist väärtust")
    return sunniaastad

def filtreeri_sunniaastad(andmete_list, min_aasta=2000, max_aasta=2025):
    if not andmete_list:
        print("Andmed puuduvad")
        return []
    sobivad = []
    sobivaid_andmeid = 0
    kokku_andmeid = 0
    for rida in andmete_list:
        kokku_andmeid += 1
        if rida < min_aasta or rida > max_aasta:
            continue
        sobivad.append(rida)
        sobivaid_andmeid += 1
    print(f"Sobivaid sünniaastaid kokku: {sobivaid_andmeid}")
    return sobivad

def arvuta_statistika(sobivad_sunniaastad):
    if not sobivad_sunniaastad:
        print("Viga: failist ei saanud andmeid lugeda.")
        return None, None, None
    kokku = 0
    andmeid_kokku = 0
    vanim = 10000000
    noorim = 0
    try:
        for read in sobivad_sunniaastad:
            kokku += read
            andmeid_kokku += 1
            if read < vanim:
                vanim = read
            else:
                vanim = vanim
            if read > noorim:
                noorim = read
            else:
                noorim = noorim
        if andmeid_kokku > 0:
            keskmine = round(kokku/andmeid_kokku)

    except Exception as e:
        print(f"Sobivaid sünniaastaid ei leitud! {e}")
        return None, None, None

    return (keskmine, vanim, noorim)

def main():

    andmete_list = lae_koik_sunniaastad_failist(failinimi = "sunniaastad_data.txt")
    sobivad_sunniaastad = filtreeri_sunniaastad(andmete_list, min_aasta=2000, max_aasta=2025)
    if sobivad_sunniaastad:
        keskmine, vanim, noorim = arvuta_statistika(sobivad_sunniaastad)
        print(f"\nKeskmine sünniaasta: {keskmine}\n"
              f"Vanim isik sünniaasta järgi: {vanim}\n"
              f"Noorim isik sünniaasta järgi: {noorim}\n")
        vanim_aasta_jargi = 2025 - vanim
        noorim_aasta_jargi = 2025- noorim
        print(f"Vanima isiku vanus 2025. aastal: {vanim_aasta_jargi} aastat\n"
              f"Noorima isiku vanus 2025. aastal: {noorim_aasta_jargi} aastat")
    else:
        print("Sobivaid sünniaastaid ei leitud!")

if __name__ == "__main__":
    main()