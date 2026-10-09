print("== SINEMA BILET FIYATI HESAPLAMA ==")
biletfiyat = None
ogrencidurum = None
yas = int(input("Lütfen yaşınızı girin: "))
if yas < 12 or yas >= 65:
    biletfiyat = 50
else:
    ogrencidurum = int(input("Öğrenci misiniz? 1: Evet, 2: Hayır: "))
    if ogrencidurum == 1:
        biletfiyat = 75
    if ogrencidurum == 2:
        biletfiyat = 100


print("Bilet fiyatınız: ",biletfiyat)