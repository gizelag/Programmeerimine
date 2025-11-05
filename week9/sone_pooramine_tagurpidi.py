def poora_sone(sone: str) -> str:
    if not isinstance(sone, str):#kontrollime kas sone on string
        print("Viga:sisend pole string")
        return " "#tagastab tuhiku
    pikkus = len(sone)#baas on sone pikkus
    if pikkus > 0:
        return sone[(pikkus-1)] + poora_sone(sone[:pikkus-1])#samm
    else:
        return ''#tagastab tuhiku

def main():
    sone = poora_sone("tere")
    print (sone)

if __name__ == '__main__':
    main()
