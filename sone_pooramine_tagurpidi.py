def poora_sone(sone: str):
    if not isinstance(sone, str):#kontrollime kas sone on string
        print("Viga:sisend pole string")
        return None
    if len(sone) == 0:#baas on sone pikkus, seadsime piiri
        return ""#tagastab tuhiku sest 0 ei saa str-is tagastada
    else:
        return sone[-1] + poora_sone(sone[:-1])#

def main():
    andmed = "tere"
    print(poora_sone(andmed))

if __name__ == "__main__":
    main()

