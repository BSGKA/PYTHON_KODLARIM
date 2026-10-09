print("=== İnternet Paketi Aşım ve Fatura Hesaplama ===")
kGB = int(input("Kullanılan GB miktarını giriniz: "))
verilmesigerekenucret = 150
ekstra = None
if kGB <0:
    print("Geçersiz kullanım miktarı")
elif kGB <= 10:
    print("Toplam fatura tutarı: ",verilmesigerekenucret)

elif kGB > 10:
        ekstra = (kGB-10)
        verilmesigerekenucret = verilmesigerekenucret+(ekstra*20)
        print("Toplam fatura tutarı: ",verilmesigerekenucret)