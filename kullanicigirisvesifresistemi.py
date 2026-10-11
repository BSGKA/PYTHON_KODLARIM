kayitli_kullanici = ""
kayitli_sifre = ""
print("== ANA MENÜ ==")
while True:
    print("1-Kayıt ol")
    print("2-Giriş yap")
    print("3-Çıkış")
    print("")
    print("")
    secim = int(input("Lütfen bir işlem numarası girin ve enter'a basın: "))

    if secim ==1:
        if kayitli_kullanici or kayitli_sifre:
            print("Zaten kayıtlı biri var!")
            input("\nEntera basarak işlem menüsünü açın..")
        else:
            kayitli_kullanici = str(input("Kullanıcı adı girin: "))
            kayitli_sifre = str(input("Şifre adı girin: "))
            print("Kayıt başarıyla oluşturuldu!")
            input("\nEntera basarak işlem menüsünü açın..")
    elif secim ==2:
        giriskullanici = str(input("Giriş için kullanıcı adı girin: "))
        girissifre = str(input("Giriş için şifre adı girin: "))
        if girissifre == "" or giriskullanici == "":
            print("Çok yanlış işlerdesin kardeşim")
            break
        if giriskullanici == kayitli_kullanici and girissifre == kayitli_sifre:
            print("Giriş yapıldı!")
            input("\nEntera basarak işlem menüsünü açın..")
        else:
            print("Kullanıcı adı veya şifre hatalı!")
            input("\nEntera basarak işlem menüsünü açın..")
    elif secim ==3:
        print("Görüşürüz")
        break
    else:
        print("Bulunmayan bir numara girdin!")