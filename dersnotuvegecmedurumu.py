vize = int(input("Vize notunuzu giriniz: "))

final = int(input("Final notunuzu giriniz: "))
ortalama = None
yanlisnot = 0
if final < 0 or final > 100:
    print("Lütfen doğru final notu girin.")
    yanlisnot = 1
if vize < 0 or vize > 100:
    print("Lütfen doğru vize notu girin.")
    yanlisnot = 1
ortalama = (vize*40)/100 + (final*60)/100
if yanlisnot != 1 and final <= 50:
    print("Maalesef Kaldınız, final notunuz düşük")
elif ortalama >=50 and yanlisnot != 1:
    print("Tebrikler, Dersi Geçtiniz! Ortalamanız:",ortalama)
elif ortalama <50 and yanlisnot != 1:
    print("Maalesef Kaldınız. Ortalamanız:",ortalama)