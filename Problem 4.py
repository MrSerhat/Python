sayı1=int(input("Sayı 1 i giriniz"))
sayı2=int(input("Sayı 2 yi giriniz"))
print("Değiştirilmeden Önce Değerler\na: {} b: {}\n".format(sayı1,sayı2))

sayı1,sayı2=sayı2,sayı1

print("Değiştirildikten Sonraki Değerler\na: {} b: {}\n".format(sayı1,sayı2))