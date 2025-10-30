def aste(alus: int, astendaja: int) -> float:

    #rekursiooni baas
    if astendaja == 0:
        return 1
    if astendaja < 0:
        return 1/alus * aste(alus,astendaja + 1)

