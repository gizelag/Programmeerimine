def leia_paeva_keskmine(paevad, paevade_temp):
    if not paevad or paevade_temp:
        print(" Viga, tühi fail")
        return {}
    if len(paevad) != len(paevade_temp):
        print("Viga, pole sama pikkusega")
        return {}
    paevade_avg_dict = {}
    try:
        paevade_avg_dict = {
            paev: round(sum(tempid) / len(tempid), 1)
            for paev, tempid in zip(paevad, paevade_temp)#uhendame
        }
        return paevade_avg_dict
    except Exception as e:
        print(f"Viga:{e}")
        return {}


def leia_ekstreemsed(paevade_avg_dict):
    if not paevade_avg_dict:
        print("Viga, leia_ekstreemsed")
        return None, None
    soojem= max(paevade_avg_dict, key=lambda x: paevade_avg_dict[x])
    kulmem= min(paevade_avg_dict, key=lambda x: paevade_avg_dict[x])
    return soojem, kulmem

def main():
    paevad = ["E", "T", "K", "N", "R", "L", "P"]

    paevade_temp = [
        [3.2, 4.1, 5.0, 2.9, 2.4] ,  # E
        [1.0, 2.3, 3.3, 2.0, 0.9],  # T
        [0.5, 1.1, 2.0, 1.6, 0.7],  # K
        [2.2, 3.0, 4.4, 3.5, 2.9],  # N
        [1.9, 1.5, 2.2, 1.7, 1.3],  # R
        [0.0, -0.5, -0.8, -1.0, -1.3],  # L
        [1.2, 1.9, 2.0, 2.5, 1.8]  # P
    ]
    paevade_avg_dict = leia_paeva_keskmine(paevad, paevade_temp)
    print(f"Päevade keskmised: {paevade_avg_dict}")
    soojem, kulmem = leia_ekstreemsed(paevade_avg_dict)
    if soojem and kulmem:
        print(f"Soojem keskmine: {soojem} ({paevade_avg_dict[soojem]})")
        print(f"Külmem keskmine: {kulmem} ({paevade_avg_dict[kulmem]})")

if __name__ == "__main__":
    main()