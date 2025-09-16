kulu = float(input("Sisesta auto keskmine kütuse kulu (1/100km: "))#kusib kasutajalt kutuse kulu
tee_pikkus = float(input("Sisesta teepikkus (km): "))#kusib kasutajalt teepikkust
kutuse_hind =float(input("Sisesta kütuse hind (€/liiter):"))#kusib kasutajalt kutuse hinda liitri kohta

kulu_liitrid = (kulu * tee_pikkus)/ 100#kulu liitri kohta arvutamie
kulu_maksumus = kulu_liitrid * kutuse_hind#kulu maksumus

#umardus kahe komakohani
print(f"Kogu teekonna jooksul kulub {round(kulu_liitrid, 2)} liitrit kütust.")
print(f"Kogu tankimise maksumus on {round(kulu, 2)} €.")