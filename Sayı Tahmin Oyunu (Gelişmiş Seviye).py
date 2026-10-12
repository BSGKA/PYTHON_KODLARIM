import random
print("=== Sayı Tahmin Oyunu ===")
ts = random.randint(1,50)
kth = 10
deneme = None
while True:
    if kth == 0:
        print("\nDeneme hakkın kalmadı, sayı buydu:",ts)
        break
    deneme=int(input("1 ile 50 arasında bir sayı tuttum! Tahmin et bakalım: "))
    if deneme < ts:
        kth=kth -1
        print("Daha büyük bir sayı! Kalan deneme hakkı:",kth)
    elif deneme > ts:
        kth=kth-1
        print("Daha küçük bir sayı! Kalan deneme hakkı:",kth)
    elif deneme == ts:
        print("\nDoğru! Sayı:",ts)
        print("== OYUNU KAZANDINIZ!! ==")
        break