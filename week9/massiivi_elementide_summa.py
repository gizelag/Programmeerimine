def massiivi_summa(massiiv: list[int]) -> int:
    if not isinstance(massiiv, list):#kontrollime kas sisend on list
        print("Viga:sisend pole list")#veateade
        return None
    if len(massiiv) == 0:#rekursiooni baas, piiriks on null
        return 0
    else:#rekursiooni samm
        return massiiv[0] + massiivi_summa(massiiv[1:])

def main():#kutsume maini valja
    andmed = [1, 2, 3, 4]
    print(massiivi_summa(andmed))

if __name__ == "__main__":
    main()
