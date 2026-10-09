print("=== Otopark Ücreti Hesaplama ===")
saat = int(input("Otoparkta ne kadar saat kaldığınızı girin: "))
ucret = None
ekstra = None
if saat <= 0:
    print("Geçersiz süre.")
elif saat <= 1:
    ucret = 30
    print("Ücret:",ucret)
elif saat >1 and saat <=5:
    ucret = 50
    print("Ücret:",ucret)
elif saat >5:
    ekstra = saat-5
    ucret = 50+(ekstra*10)
    print("Ücret:",ucret)