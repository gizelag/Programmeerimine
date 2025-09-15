arv = int(input("sisesta taisarv: "))#kusib kasutajalt taisarvu
#kontrollime kas jagub
if arv / 3 and arv / 5:print("see arv jagub nii 3 kui ka 5-ga")#kui arv 3 ja 5-ga jagub ja jaak on 0
elif arv / 3:print("see arv jagub 3-ga")#kui arv jagub 3-ga ja jaak on 0
elif arv / 5:print("see arv jagub 5-ga")#kui jagub 5-ga
else: print("see arv ei jagu 3 ega 5-ga")#kui ei jagu kummagagi