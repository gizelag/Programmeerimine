def kahendotsing(sorteeritud_massiiv: list[int], otsitav: int, algus: int, lopp: int) -> int:
    if not isinstance(otsitav, int):
        print("Viga")
        return None
#massiv on eri andmete kogum uhes muutujas
    if isinstance(sorteeritud_massiiv, list):

        keskmine = (algus+lopp) // 2
        if otsitav > sorteeritud_massiiv[lopp]:
            return None
        if otsitav < sorteeritud_massiiv[algus]:
            return None
        if sorteeritud_massiiv[keskmine] == otsitav:
            return keskmine
        elif otsitav > sorteeritud_massiiv[keskmine]:
            return kahendotsing(sorteeritud_massiiv,otsitav, keskmine +1, lopp)
        else:
            return kahendotsing(sorteeritud_massiiv,otsitav, algus, keskmine-1)

    else:
        print("Viga")
        return None
def main():
    sorteeritud_massiiv = [1, 2, 3, 4]
    otsitav = 0


