
def integer_to_roman(number):
    # Kontrollime, et arv oleks vahemikus 1–1000
    if number < 1 or number > 1000:
        return "Arv peab olema vahemikus 1 kuni 1000"

    # Rooma numbrite väärtused ja sümbolid konventeerimiseks
    vaartused = [1000, 900, 500, 400, 100, 90, 50, 40,
              10, 9, 5, 4, 1]
    symbolid = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
               "X", "IX", "V", "IV", "I"]

    tulemus = ""  #siia tuleb tulemus

    # Läbime siin kõik väärtused
    for i in range(len(vaartused)):
        # Kuni number on suurem või võrdne väärtusega
        while number >= vaartused[i]:
            tulemus += symbolid[i]   # Lisame sümboli
            number -= vaartused[i]    # Lahutame väärtuse

    return tulemus


# Näited
print(integer_to_roman(3))     # III
print(integer_to_roman(58))    # LVIII
print(integer_to_roman(199))   # CXCIX
print(integer_to_roman(1000))  # M