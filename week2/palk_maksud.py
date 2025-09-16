brutopalk = float(input("sisesta brutopalk (€):"))
komakohad = int(input("sisesta komakohad (1 voi 2):"))
tulumaks = brutopalk * 0.22
sotsiaalmaks = brutopalk * 0.33
toostuskindlustusmaks = brutopalk * 0.016
netopalk = brutopalk - tulumaks - toostuskindlustusmaks


if komakohad == 1:
    print(f"Palgaarvestuse kokkuvõte: \n Brutopalk: {brutopalk:.1f}€\n Tulumaks (22%): {tulumaks:.1f}€ \n Sotsiaalmaks (33%): {sotsiaalmaks:.1f}€ (tööandja maksab) \n Tööstuskindlustus (1.6%): {toostuskindlustusmaks:.1f}€ \n Netopalk (kätte saadav summa): {netopalk:.1f}€ ")
if komakohad == 2:
    print(f"Palgaarvestuse kokkuvõte: \n Brutopalk: {brutopalk:.2f}€\n Tulumaks (22%): {tulumaks:.2f}€ \n Sotsiaalmaks (33%): {sotsiaalmaks:.2f}€ (tööandja maksab) \n Tööstuskindlustus (1.6%): {toostuskindlustusmaks:.2f}€ \n Netopalk (kätte saadav summa): {netopalk:.2f}€ ")




