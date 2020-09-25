boy=float(input("Boy: (Metre olarak giriniz)"))
kilo=int(input("Kilo:"))
bki=kilo/(boy*boy)
if bki<18.5:
    print("zayıf",bki)
elif bki>18.5 and bki<25:
    print("normal",bki)
elif bki > 25 and bki < 30:
    print("fazla kilolu",bki)
elif bki >30:
    print("obez",bki)


