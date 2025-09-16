import math#impordin math mooduli matemaatiliste funktsioonide jaoks

#kusib kasutajalt andmeid
v = float(input("Sisesta algkiirus (m/s): "))
nurk_kraadides = float(input("Sisesta hüppe nurk (kraadi): "))

#teisendamine radiaanideks
nurk_radiaanides = math.radians(nurk_kraadides)

#valem
g = 9.81
kaugus = (v **2) *math.sin(2 * nurk_radiaanides) / g

#tulemus tuleb valjastada kahe koma kohaga
print(f"Sa hüppad {kaugus:.2f}meetrit kaugele")