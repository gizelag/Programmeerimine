def kahendotsing(sorteeritud_massiiv: list[int], otsitav: int, algus: int, lopp: int) -> int:
    # otsitav peab olema täisarv
    if not isinstance(otsitav, int):
        print("Viga")
        return None

    # kontrollime, et antud andmed oleksid listis
    if isinstance(sorteeritud_massiiv, list):

        # leiame vahemiku keskmise indeksi
        keskmine = (algus + lopp) // 2

        # kui otsitav on väiksem kui esimene element
        if otsitav < sorteeritud_massiiv[algus]:
            return None

        # kui otsitav on suurem kui viimane element
        if otsitav > sorteeritud_massiiv[lopp]:
            return None

        # kui keskmine element on otsitav
        if sorteeritud_massiiv[keskmine] == otsitav:
            return keskmine

        # kui otsitav on suurem, otsime paremast poolest
        elif otsitav > sorteeritud_massiiv[keskmine]:
            return kahendotsing(
                sorteeritud_massiiv,
                otsitav,
                keskmine + 1,
                lopp
            )

        # muidu otsime vasakust poolest
        else:
            return kahendotsing(
                sorteeritud_massiiv,
                otsitav,
                algus,
                keskmine - 1
            )

    # kui massiiv pole list
    print("Viga")
    return None


def main():
    sorteeritud_massiiv = [1, 2, 3, 4]
    otsitav = 0

    tulemus = kahendotsing(sorteeritud_massiiv, otsitav, 0, len(sorteeritud_massiiv) - 1)
    print(tulemus)
