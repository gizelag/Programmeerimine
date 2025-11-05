def aste(alus, astendaja):
    if isinstance(alus, int):
        if isinstance(astendaja, int):
            if astendaja == 0:
                return 1
            if astendaja > 0 :
                return alus * aste(alus, astendaja-1)

            if astendaja < 0: #Neg astendaja
                return 1/alus * aste(alus, astendaja+1)
        else:
            print("Viga")
            return None
    else:
        print("Viga")
        return None

def main():
    vastus=aste(5,2.2)
    print(vastus)

if __name__ == '__main__':
    main()




'''def aste(alus: int, astendaja: int) -> float:

    #rekursiooni baas
    if astendaja == 0:
        return 1
    if astendaja < 0:
        return 1/alus * aste(alus,astendaja + 1)'''

