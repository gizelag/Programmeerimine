def aste(alus, astendaja):
    # Kontrollime, et alus oleks täisarv
    if isinstance(alus, int):

        # Kontrollime, et astendaja oleks täisarv
        if isinstance(astendaja, int):

            # Kui astendaja on 0, siis vastus on alati 1
            # (nt 5^0 = 1)
            if astendaja == 0: #baas
                return 1

            # Kui astendaja on positiivne
            # korrutame aluse iseendaga nii mitu korda,
            # kasutades rekursiooni
            if astendaja > 0:#samm
                return alus * aste(alus, astendaja - 1)

            # Kui astendaja on negatiivne
            # jagame 1 alusega ja liigume samm-sammult nulli poole
            if astendaja < 0:
                return 1 / alus * aste(alus, astendaja + 1)

        else:
            # Astendaja ei ole täisarv
            print("Viga")
            return None
    else:
        # Alus ei ole täisarv
        print("Viga")
        return None


def main():
    # Testime funktsiooni vale sisendiga (astendaja pole int)
    vastus = aste(5, 2.2)

    # Prindime tulemuse
    print(vastus)


if __name__ == '__main__':
    main()




'''def aste(alus: int, astendaja: int) -> float:

    #rekursiooni baas
    if astendaja == 0:
        return 1
    if astendaja < 0:
        return 1/alus * aste(alus,astendaja + 1)'''

