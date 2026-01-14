def numbrite_summa(arv: int):
    # kontrollime, et oleks täisarv
    if isinstance(arv, int):

        # negatiivse arvu muudame positiivseks
        arv = abs(arv)

        # BAAS: kui on üks number, siis tagastame selle
        if arv < 10:
            return arv

        # SAMM: võtame viimase numbri ja liidame ülejäänu summa
        return arv % 10 + numbrite_summa(arv // 10)

    # kui sisend pole täisarv
    print("Viga")
    return None


def main():
    arv = -198
    print(numbrite_summa(arv))


if __name__ == '__main__':
    main()
