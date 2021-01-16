import random
import time

print("""
*****************************
Zar atma oyununa hoşgeldiniz.

-Zar atmak için 'e'
-Çıkış yapmak için 'q'
*****************************
""")

min = 1
maks = 6

baslat = input("Zarlar atılsın mı? ")
tekrar = "Zarlar tekrar atılıyor..."

while True:
    if baslat == "q" or tekrar == "q":
        print("Program sonlandırılıyor...")
        break
    elif baslat == "e" or tekrar == "e":
        print("Zarlar atılıyor...")
        time.sleep(1)
        print(random.randint(min,maks))
        print(random.randint(min,maks))
        tekrar = input("Zarlar tekrar atılsın mı?")
    else:
        print("Lütfen geçerli değerler giriniz...")
        break