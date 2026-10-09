print("== PYTHON'DA 4 İŞLEMLER ==")
print("--------------------------")
print("1 - Toplama")
print("2 - Çıkartma")
print("3 - Çarpma")
print("4 - Bölme")
secim = int(input("Lütfen bir işlem seçin: "))
sayi1 = None
sayi2 = None
sonuc = None
if secim == 1:
    print("Toplama için 2 sayı giriniz.")
    sayi1 = int(input("1. sayıyı girin: "))
    sayi2 = int(input("2. sayıyı girin: "))
    sonuc = sayi1+sayi2
elif secim == 2:
    print("Çıkartma için 2 sayı giriniz.")
    sayi1 = int(input("1. sayıyı girin: "))
    sayi2 = int(input("2. sayıyı girin: "))
    sonuc = sayi1-sayi2
elif secim == 3:
    print("Çarpma için 2 sayı giriniz.")
    sayi1 = int(input("1. sayıyı girin: "))
    sayi2 = int(input("2. sayıyı girin: "))
    sonuc = sayi1*sayi2
elif secim == 4:
    print("Bölme için 2 sayı giriniz.")
    sayi1 = int(input("1. sayıyı girin: "))
    sayi2 = int(input("2. sayıyı girin: "))
    sonuc = sayi1/sayi2


print("Sonuç =", int(sonuc))
