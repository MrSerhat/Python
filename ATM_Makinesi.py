print(""" 
***********************************
      Atm Makinesine Hoşgeldiniz:
    İşlemler;
    
    1.Bakiye Sorgulama
    
    2.Para yatırma
    
    3.Para Çekme
    
    Programdan çıkmak için 'q'  ya basın.
***********************************   
    """)
bakiye= 1000

while True:
    işlem=input("İşlemi seçiniz:")

    if(işlem=="q"):
        print("Yine bekleriz")
        break

    elif(işlem=="1"):
        print("Bakiyeniz {} tl dir.".format(bakiye))

    elif (işlem == "2"):

        miktar=int(input("Miktarı Giriniz:"))
        bakiye += miktar

    elif (işlem == "3"):
        miktar=int(input("Miktarı giriniz"))

        if (bakiye-miktar<0):
            print("Bakiye yetersiz...")
            continue
        bakiye-=miktar
        print("Bakiyeniz {} tl dir.".format(bakiye))

    else:
        print("Geçersiz işlem...")