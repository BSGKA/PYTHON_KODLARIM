secim = None
hesapbakiyesi = 1000
while True:
    print("== ANA MENÜ ==")
    print("1 - Bakiye Sorgulama")
    print("2 - Para Çek")
    print("3 - Para Yatır")
    print("4 - Çıkış")
    print("")
    print("")
    print("")
    secim = int(input("Lütfen istediğiniz işlemin numarasını girip enter'a basın: "))
    if secim == 1:
        print("Hesap bakiyeniz:",hesapbakiyesi)
        input("\nAna menüye dönmek için Enter'a basın...")
    elif secim == 2:
        para_cek = int(input("Çekmek istediğiniz miktarı girin: "))
        if para_cek > hesapbakiyesi:
            print("Yetersiz bakiye!")
            input("\nAna menüye dönmek için Enter'a basın...")
        else:
            hesapbakiyesi = hesapbakiyesi-para_cek
            print("Kalan bakiye:",hesapbakiyesi)
            input("\nAna menüye dönmek için Enter'a basın...")
    elif secim == 3:
        yatirma = int(input("Yatırmak istediğiniz para miktarı: "))
        hesapbakiyesi=yatirma+hesapbakiyesi
        print("Hesap bakiyeniz:",hesapbakiyesi)
        input("\nAna menüye dönmek için Enter'a basın...")
    elif secim==4:
        print("İyi günler dileriz...")
        break
    else:
        print("Geçersiz işlem!")
        input("\nAna menüye dönmek için Enter'a basın...")