print("""**************************************
Sayı tahmin uygulamasına hoşgeldiniz.
**************************************

Lütfen aklınızdan bir sayı tutunuz.

""")

while True:
    a = 0
    baslangic = input("Başlamak için 's' , Çıkmak için 'q' yazınız: ")
    if baslangic == "q":
        print("Program sonlandırılıyor....")
        break
    
    elif baslangic == "s":
        adım1 = int(input("Aklınızdaki sayıyla toplamak için bir değeri girin: "))

        a += adım1

        adım2 = int(input("Çıkan sonuçtan çıkartmak için bir değer girin: "))

        a -= adım2

        adım3 = int(input("Çıkan sonucu çarpmak için bir değer girin: "))

        a *= adım3

        adım4 = int(input("Çıkan sonucu girin: "))


        b = (adım4 / adım3) + (adım2 - adım1)

        print("İlk başta aklınızdan tuttuğunu sayı:", b)
    
    else:
        print("Lütfen sadece belirtilen değerleri kullanınız.")



