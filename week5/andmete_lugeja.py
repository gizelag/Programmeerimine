def loe_tekst_failist(failinimi):
    try:
        with open(failinimi, 'r', encoding='utf-8') as fail:
            tekst = fail.read().strip()
            #eemaldame tuhikud lopust
            return tekst
    except FileNotFoundError:
        print("Viga, faili ei leitud")
        return None
    except Exception as e:
        print("Tundmatu viga")
        return None

if __name__ == '__main__':
    loe_tekst_failist(failinimi)
    tekst = loe_tekst_failist(failinimi)
    print(tekst)