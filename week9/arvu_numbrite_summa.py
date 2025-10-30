def numbrite_summa(arv: int) -> int:
    if isinstance(arv, int):
        arv = abs(arv)
        if (arv) < 10:
            return arv
        return (arv) % 10 + numbrite_summa(arv // 10)
    else:
        print("Viga")
        return

def main():
    arv = (-198)
    print(numbrite_summa(arv))

if __name__ == '__main__':
    main()