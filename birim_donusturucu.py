print ("=> Birim Dönüştürme Programına Hoşgeldiniz.=>")

print ("""
BİRİM LİSTESİ :
[0] Programdan Çıkış
[1] Uzunluk Birimleri :
    [A] Milimetre (mm)
    [B] Santimetre (cm)
    [C] Desimetre (dm)
    [D] Metre (m)
    [E] Dekametre (dam)
    [F] Hektometre (hm)
    [G] Kilometre (km)
[2] Sıcaklık Birimleri :
    [A] Celsius (Santigrat) (°C)
    [B] Fahrenheit (Fahrenhayt) (°F)
    [C] Kelvin (°K)
[3] Kütle Birimleri
    [A] Gram (g)
    [B] Dekagram (dag)
    [C] Hektogram (hg)
    [D] Kilogram (kg)
    [E] Ton (t)
[4] Alan Birimleri
    [A] Milimetrekare (mm²)
    [B] Santimetrekare (cm²)
    [C] Desimetre (dm²)
    [D] Metre (m²)
    [E] Dekametrekare (dam²)
    [F] Hektometrekare (hm²)
    [G] Kilometrekare (km²)
""")

while True :
    birim_seçimi = int(input("Hangi birim türünde çevirmek istiyorsunuz? Listeden rakamlarla seçiniz. : "))

    if birim_seçimi == 0 :
        print ("Programdan Çıkılıyor...")
        break 

    elif birim_seçimi == 1 :
        uzunluk = input ("Hangi uzunluk birimini çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
        if uzunluk == "A" or uzunluk == "a" :
            uzunluk2 = input ("Milimetre birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if uzunluk2 == "A" or uzunluk2 == "a" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif uzunluk2 == "B" or uzunluk2 == "b":
                sayı = float(input("Kaç milimetreyi santimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10
                print ("{} milimetre {} santimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "C" or uzunluk2 == "c":
                sayı = float(input("Kaç milimetreyi desimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} milimetre {} desimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "D" or uzunluk2 == "d":
                sayı = float(input("Kaç milimetreyi metreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000
                print ("{} milimetre {} metreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "E" or uzunluk2 == "e":
                sayı = float(input("Kaç milimetreyi dekametreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10000
                print ("{} milimetre {} dekametreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "F" or uzunluk2 == "f":
                sayı = float(input("Kaç milimetreyi hektometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100000
                print ("{} milimetre {} hektometreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "G" or uzunluk2 == "g":
                sayı = float(input("Kaç milimetreyi kilometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000000
                print ("{} milimetre {} kilometreye eşittir." .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")

        elif uzunluk == "B" or uzunluk == "b" :
            uzunluk2 = input ("Santimetre birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if uzunluk2 == "B" or uzunluk2 == "b" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif uzunluk2 == "A" or uzunluk2 == "a":
                sayı = float(input("Kaç santimetreyi milimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10
                print ("{} santimetre {} milietreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "C" or uzunluk2 == "c":
                sayı = float(input("Kaç santimetreyi desimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10
                print ("{} santimetre {} desimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "D" or uzunluk2 == "d":
                sayı = float(input("Kaç santimetreyi metreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} santimetre {} metreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "E" or uzunluk2 == "e":
                sayı = float(input("Kaç santimetreyi dekametreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000
                print ("{} santimetre {} dekametreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "F" or uzunluk2 == "f":
                sayı = float(input("Kaç milimetreyi hektometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10000
                print ("{} santimetre {} hektometreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "G" or uzunluk2 == "g":
                sayı = float(input("Kaç milimetreyi kilometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100000
                print ("{} santimetre {} kilometreye eşittir." .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")

        elif uzunluk == "C" or uzunluk == "c" :
            uzunluk2 = input ("Desimetre birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if uzunluk2 == "C" or uzunluk2 == "c" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif uzunluk2 == "A" or uzunluk2 == "a":
                sayı = float(input("Kaç desimetreyi milimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} desimetre {} milimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "B" or uzunluk2 == "b":
                sayı = float(input("Kaç desimetreyi desimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10
                print ("{} desimetre {} santimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "D" or uzunluk2 == "d":
                sayı = float(input("Kaç desimetreyi metreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10
                print ("{} desimetre {} metreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "E" or uzunluk2 == "e":
                sayı = float(input("Kaç desimetreyi dekametreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} desimetre {} dekametreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "F" or uzunluk2 == "f":
                sayı = float(input("Kaç desimetreyi hektometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000
                print ("{} desimetre {} hektometreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "G" or uzunluk2 == "g":
                sayı = float(input("Kaç desimetreyi kilometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10000
                print ("{} desimetre {} kilometreye eşittir." .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")

        elif uzunluk == "D" or uzunluk == "d" :
            uzunluk2 = input ("Metre birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if uzunluk2 == "D" or uzunluk2 == "d" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif uzunluk2 == "A" or uzunluk2 == "a":
                sayı = float(input("Kaç metreyi milimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000
                print ("{} metre {} milimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "B" or uzunluk2 == "b":
                sayı = float(input("Kaç metreyi santimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} metre {} santimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "C" or uzunluk2 == "c":
                sayı = float(input("Kaç metreyi metreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10
                print ("{} metre {} desimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "E" or uzunluk2 == "e":
                sayı = float(input("Kaç metreyi dekametreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10
                print ("{} metre {} dekametreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "F" or uzunluk2 == "f":
                sayı = float(input("Kaç metreyi hektometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} metre {} hektometreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "G" or uzunluk2 == "g":
                sayı = float(input("Kaç metreyi kilometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000
                print ("{} metre {} kilometreye eşittir." .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")
        
        elif uzunluk == "E" or uzunluk == "e" :
            uzunluk2 = input ("Dekametre birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if uzunluk2 == "E" or uzunluk2 == "e" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif uzunluk2 == "A" or uzunluk2 == "a":
                sayı = float(input("Kaç dekametreyi milimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10000
                print ("{} dekametre {} milimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "B" or uzunluk2 == "b":
                sayı = float(input("Kaç dekametreyi santimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000
                print ("{} dekametre {} santimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "C" or uzunluk2 == "c":
                sayı = float(input("Kaç dekametreyi metreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} dekametre {} desimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "D" or uzunluk2 == "d":
                sayı = float(input("Kaç dekametreyi metreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10
                print ("{} dekametre {} metreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "F" or uzunluk2 == "f":
                sayı = float(input("Kaç dekametreyi hektometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10
                print ("{} dekametre {} hektometreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "G" or uzunluk2 == "g":
                sayı = float(input("Kaç dekametreyi kilometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} metre {} kilometreye eşittir." .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")
        
        elif uzunluk == "F" or uzunluk == "f" :
            uzunluk2 = input ("Hektometre birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if uzunluk2 == "F" or uzunluk2 == "f" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif uzunluk2 == "A" or uzunluk2 == "a":
                sayı = float(input("Kaç hektometreyi milimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100000
                print ("{} hektometre {} milimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "B" or uzunluk2 == "b":
                sayı = float(input("Kaç hektometreyi santimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10000
                print ("{} hektometre {} santimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "C" or uzunluk2 == "c":
                sayı = float(input("Kaç hektometreyi desimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000
                print ("{} hektometre {} desimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "D" or uzunluk2 == "d":
                sayı = float(input("Kaç hektometreyi metreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} hektometre {} metreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "E" or uzunluk2 == "e":
                sayı = float(input("Kaç hektometreyi dekametreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10
                print ("{} hektometre {} dekametreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "G" or uzunluk2 == "g":
                sayı = float(input("Kaç hektometreyi kilometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10
                print ("{} hektometre {} kilometreye eşittir." .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")

        elif uzunluk == "G" or uzunluk == "g" :
            uzunluk2 = input ("Hektometre birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if uzunluk2 == "G" or uzunluk2 == "g" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif uzunluk2 == "A" or uzunluk == "a":
                sayı = float(input("Kaç kilometreyi milimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000000
                print ("{} kilometre {} milimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "B" or uzunluk2 == "b":
                sayı = float(input("Kaç kilometreyi santimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100000
                print ("{} kilometre {} santimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "C" or uzunluk2 == "c":
                sayı = float(input("Kaç kilometreyi desimetreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10000
                print ("{} kilometre {} desimetreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "D" or uzunluk2 == "d":
                sayı = float(input("Kaç kilometreyi metreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000
                print ("{} kilometre {} metreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "E" or uzunluk2 == "e":
                sayı = float(input("Kaç kilometreyi dekametreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} kilometre {} dekametreye eşittir." .format(sayı,sonuç))
            elif uzunluk2 == "F" or uzunluk2 == "f":
                sayı = float(input("Kaç kilometreyi hektometreye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10
                print ("{} kilometre {} hektometreye eşittir." .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")
        else :
                print ("Yanlış seçim yaptınız!")

    elif birim_seçimi == 2 :
        sıcaklık = input("Hangi sıcaklık birimini çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
        if sıcaklık == "A" or sıcaklık == "a" :
            sıcaklık2 = input("Celsius'u hangi birime çevirmek istiyorsunuz? : ")
            if sıcaklık2 == "A" or sıcaklık2 == "a" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif sıcaklık2 == "B" or sıcaklık2 == "b" :
                sayı = float(input("Kaç Celsius'u Fahrenheit'a çevirmek istiyorsunuz? : "))
                sonuç = (sayı * 1.8) + 32
                print ("{} Celsius {} Fahrenheit'a eşittir." .format(sayı,sonuç))
            elif sıcaklık2 == "C" or sıcaklık2 == "c" :
                sayı = float(input("Kaç Celsius'u Kelvin'e çevirmek istiyorsunuz? : "))
                sonuç = sayı + 273.15
                print ("{} Celsius {} Kelvin'e eşittir." .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")
        elif sıcaklık == "B" or sıcaklık == "b" :
            sıcaklık2 = input("Fahrenheit'u hangi birime çevirmek istiyorsunuz? : ")
            if sıcaklık2 == "B" or sıcaklık2 == "b" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            if sıcaklık2 == "A" or sıcaklık2 == "a" :
                sayı = float(input("Kaç Fahrenheit'ı Celsius'a çevirmek istiyorsunuz? : "))
                sonuç = (sayı - 32) / 1.8
                print ("{} Fahrenheit {} Celsius'a eşittir." .format(sayı,sonuç))
            elif sıcaklık2 == "C" or sıcaklık2 == "c" :
                sayı = float(input("Kaç Fahrenheit'ı Kelvin'e çevirmek istiyorsunuz? : "))
                sonuç = ((sayı - 32) / 1.8) + 273.15
                print ("{} Fahrenheit {} Kelvin'e eşittir." .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")
        elif sıcaklık == "C" or sıcaklık == "c" :
            sıcaklık2 = input("Kelvin'i hangi birime çevirmek istiyorsunuz? : ")
            if sıcaklık2 == "C" or sıcaklık2 == "c" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif sıcaklık2 == "A" or sıcaklık2 == "a" :
                sayı = float(input("Kaç Kelvin'i Celsius'a çevirmek istiyorsunuz? : "))
                sonuç = sayı - 273.15
                print ("{} Kelvin {} Celsius'a eşittir." .format(sayı,sonuç))
            elif sıcaklık2 == "B" or sıcaklık2 == "b" :
                sayı = float(input("Kaç Kelvin'i Fahrenheit'a çevirmek istiyorsunuz? : "))
                sonuç = ((sayı - 273.15)*1.8) + 32
                print ("{} Kelvin {} Fahrenheit'a eşittir." .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")        
        else :
                print ("Yanlış seçim yaptınız!")

    elif birim_seçimi == 3 :
        kütle = input("Hangi kütle birimini çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
        if kütle == "A" or kütle == "a" :
            kütle2 = input("Gram birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if kütle2 == "A" or kütle2 == "a" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif kütle2 == "B" or kütle2 == "b" :
                sayı = float(input("Kaç gramı dekagrama çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10
                print ("{} gram {} dekagrama eşittir." .format (sayı,sonuç))
            elif kütle2 == "C" or kütle2 == "c" :
                sayı = float(input("Kaç gramı hektograma çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} gram {} hektograma eşittir." .format (sayı,sonuç))
            elif kütle2 == "D" or kütle2 == "d" :
                sayı = float(input("Kaç gramı kilogram çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000
                print ("{} gram {} kilograma eşittir." .format (sayı,sonuç))
            elif kütle2 == "E" or kütle2 == "e" :
                sayı = float(input("Kaç gramı tona çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000000
                print ("{} gram {} tona eşittir." .format (sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!") 
        elif kütle == "B" or kütle == "b" :
            kütle2 = input("Dekagram birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if kütle2 == "B" or kütle2 == "b" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif kütle2 == "A" or kütle2 == "a" :
                sayı = float(input("Kaç dekagramı grama çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10
                print ("{} dekagram {} grama eşittir." .format (sayı,sonuç))
            elif kütle2 == "C" or kütle2 == "c" :
                sayı = float(input("Kaç dekagramı hektograma çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10
                print ("{} dekagram {} hektograma eşittir." .format (sayı,sonuç))
            elif kütle2 == "D" or kütle2 == "d" :
                sayı = float(input("Kaç dekagramı kilograma çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} dekagram {} kilograma eşittir." .format (sayı,sonuç))
            elif kütle2 == "E" or kütle2 == "e" :
                sayı = float(input("Kaç dekagramı tona çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100000
                print ("{} dekagram {} tona eşittir." .format (sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")
        elif kütle == "C" or kütle == "c" :
            kütle2 = input("Dekagram birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if kütle2 == "C" or kütle2 == "c" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif kütle2 == "A" or kütle2 == "a" :
                sayı = float(input("Kaç hektogramı grama çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} hektogram {} grama eşittir." .format (sayı,sonuç))
            elif kütle2 == "B" or kütle2 == "b" :
                sayı = float(input("Kaç hektogramı dekagrama çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10
                print ("{} hektogram {} dekagrama eşittir." .format (sayı,sonuç))
            elif kütle2 == "D" or kütle2 == "d" :
                sayı = float(input("Kaç hektogramı kilograma çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10
                print ("{} hektogram {} kilograma eşittir." .format (sayı,sonuç))
            elif kütle2 == "E" or kütle2 == "e" :
                sayı = float(input("Kaç hektogramı tona çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10000
                print ("{} hektogram {} tona eşittir." .format (sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")
        elif kütle == "D" or kütle == "d" :
            kütle2 = input("Kilogram birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if kütle2 == "D" or kütle2 == "d" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif kütle2 == "A" or kütle2 == "a" :
                sayı = float(input("Kaç kilogramı grama çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000
                print ("{} kilogram {} grama eşittir." .format (sayı,sonuç))
            elif kütle2 == "B" or kütle2 == "b" :
                sayı = float(input("Kaç kilogramı dekagrama çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} kilogram {} dekagrama eşittir." .format (sayı,sonuç))
            elif kütle2 == "C" or kütle2 == "c" :
                sayı = float(input("Kaç kilogramı hektograma çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10
                print ("{} hektogram {} kilograma eşittir." .format (sayı,sonuç))
            elif kütle2 == "E" or kütle2 == "e" :
                sayı = float(input("Kaç kilogramı tona çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000
                print ("{} kilogram {} tona eşittir." .format (sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")
        elif kütle == "E" or kütle == "e" :
            kütle2 = input("Ton birimini hangi birime çevirmek istiyorsunuz? Listedeki harflerle seçiniz. : ")
            if kütle2 == "E" or kütle2 == "e" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif kütle2 == "A" or kütle2 == "a" :
                sayı = float(input("Kaç tonu grama çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000000
                print ("{} ton+ {} grama eşittir." .format (sayı,sonuç))
            elif kütle2 == "B" or kütle2 == "b" :
                sayı = float(input("Kaç ton dekagrama çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100000
                print ("{} ton {} dekagrama eşittir." .format (sayı,sonuç))
            elif kütle2 == "C" or kütle2 == "c" :
                sayı = float(input("Kaç tonu hektograma çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10000
                print ("{} tonu {} kilograma eşittir." .format (sayı,sonuç))
            elif kütle2 == "D" or kütle2 == "d" :
                sayı = float(input("Kaç tonu kilograma çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000
                print ("{} ton {} kilograma eşittir." .format (sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")

    elif birim_seçimi == 4 :
        alan = input("Hangi alan birimini çevirmek istiyorsunuz? Listeden harflerle seçiniz. : ")
        if alan == "A" or alan == "a" :
            alan2 = input("Milimetrekare birimini hangi birime çevirmek istiyorsunuz? : ")
            if alan2 == "A" or alan2 == "a" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif alan2 == "B" or alan2 == "b" :
                sayı = float(input("Kaç milimetrekareyi santimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} milimetrekare {} santimetrekereye eşittir. " .format(sayı,sonuç))
            elif alan2 == "C" or alan2 == "c" :
                sayı = float(input("Kaç milimetrekareyi desimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10000
                print ("{} milimetrekare {} desimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "D" or alan2 == "d" :
                sayı = float(input("Kaç milimetrekareyi metrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000000
                print ("{} milimetrekare {} metrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "E" or alan2 == "e" :
                sayı = float(input("Kaç milimetrekareyi dekametrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100000000
                print ("{} milimetrekare {} dekametrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "F" or alan2 == "f" :
                sayı = float(input("Kaç milimetrekareyi hektometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10000000000
                print ("{} milimetrekare {} hektometrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "G" or alan2 == "g" :
                sayı = float(input("Kaç milimetrekareyi kilometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000000000000
                print ("{} milimetrekare {} kilometrekareye eşittir. " .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")

        elif alan == "B" or alan == "b" :
            alan2 = input("Santimetrekare birimini hangi birime çevirmek istiyorsunuz? : ")
            if alan2 == "B" or alan2 == "b" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif alan2 == "A" or alan2 == "a" :
                sayı = float(input("Kaç santimetrekareyi milimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} santimetrekare {} milimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "C" or alan2 == "c" :
                sayı = float(input("Kaç santimetrekareyi desimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} santimetrekare {} desimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "D" or alan2 == "d" :
                sayı = float(input("Kaç santimetrekareyi metrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10000
                print ("{} santimetrekare {} metrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "E" or alan2 == "e" :
                sayı = float(input("Kaç santimetrekareyi dekametrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000000
                print ("{} santimetrekare {} dekametrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "F" or alan2 == "f" :
                sayı = float(input("Kaç santimetrekareyi hektometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100000000
                print ("{} santimetrekare {} hektometrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "G" or alan2 == "g" :
                sayı = float(input("Kaç santimetrekareyi kilometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10000000000
                print ("{} milimetrekare {} kilometrekareye eşittir. " .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")

        elif alan == "C" or alan == "c" :
            alan2 = input("Desimetrekare birimini hangi birime çevirmek istiyorsunuz? : ")
            if alan2 == "C" or alan2 == "c" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif alan2 == "A" or alan2 == "a" :
                sayı = float(input("Kaç desimetrekareyi milimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10000
                print ("{} desimetrekare {} milimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "B" or alan2 == "b" :
                sayı = float(input("Kaç desimetrekareyi santimetrekareyi çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} desimetrekare {} santimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "D" or alan2 == "d" :
                sayı = float(input("Kaç desimetrekareyi metrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} desimetrekare {} metrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "E" or alan2 == "e" :
                sayı = float(input("Kaç desimetrekareyi dekametrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10000
                print ("{} desimetrekare {} dekametrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "F" or alan2 == "f" :
                sayı = float(input("Kaç desimetrekareyi hektometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000000
                print ("{} desimetrekare {} hektometrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "G" or alan2 == "g" :
                sayı = float(input("Kaç desimetrekareyi kilometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100000000
                print ("{} desimetrekare {} kilometrekareye eşittir. " .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")

        elif alan == "D" or alan == "d" :
            alan2 = input("Metrekare birimini hangi birime çevirmek istiyorsunuz? : ")
            if alan2 == "D" or alan2 == "d" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif alan2 == "A" or alan2 == "a" :
                sayı = float(input("Kaç metrekareyi milimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000000
                print ("{} metrekare {} milimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "B" or alan2 == "b" :
                sayı = float(input("Kaç metrekareyi santimetrekareyi çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10000
                print ("{} metrekare {} santimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "C" or alan2 == "c" :
                sayı = float(input("Kaç metrekareyi desimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} metrekare {} desimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "E" or alan2 == "e" :
                sayı = float(input("Kaç metrekareyi dekametrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} metrekare {} dekametrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "F" or alan2 == "f" :
                sayı = float(input("Kaç metrekareyi hektometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10000
                print ("{} metrekare {} hektometrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "G" or alan2 == "g" :
                sayı = float(input("Kaç metrekareyi kilometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 1000000
                print ("{} metrekare {} kilometrekareye eşittir. " .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")
        
        elif alan == "E" or alan == "e" :
            alan2 = input("Dekametrekare birimini hangi birime çevirmek istiyorsunuz? : ")
            if alan2 == "E" or alan2 == "e" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif alan2 == "A" or alan2 == "a" :
                sayı = float(input("Kaç dekametrekareyi milimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100000000
                print ("{} dekametrekare {} milimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "B" or alan2 == "b" :
                sayı = float(input("Kaç dekametrekareyi santimetrekareyi çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000000
                print ("{} dekametrekare {} santimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "C" or alan2 == "c" :
                sayı = float(input("Kaç dekametrekareyi desimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10000
                print ("{} dekametrekare {} desimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "D" or alan2 == "d" :
                sayı = float(input("Kaç dekametrekareyi metrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} dekametrekare {} metrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "F" or alan2 == "f" :
                sayı = float(input("Kaç dekametrekareyi hektometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} dekametrekare {} hektometrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "G" or alan2 == "g" :
                sayı = float(input("Kaç dekametrekareyi kilometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 10000
                print ("{} dekametrekare {} kilometrekareye eşittir. " .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")

        elif alan == "F" or alan == "f" :
            alan2 = input("Hektometrekare birimini hangi birime çevirmek istiyorsunuz? : ")
            if alan2 == "E" or alan2 == "e" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif alan2 == "A" or alan2 == "a" :
                sayı = float(input("Kaç hektometrekareyi milimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10000000000
                print ("{} hektometrekare {} milimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "B" or alan2 == "b" :
                sayı = float(input("Kaç hektometrekareyi santimetrekareyi çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100000000
                print ("{} hektometrekare {} santimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "C" or alan2 == "c" :
                sayı = float(input("Kaç hektometrekareyi desimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000000
                print ("{} hektometrekare {} desimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "D" or alan2 == "d" :
                sayı = float(input("Kaç hektometrekareyi metrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10000
                print ("{} hektometrekare {} metrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "E" or alan2 == "e" :
                sayı = float(input("Kaç hektometrekareyi dekametrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} hektometrekare {} dekametrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "G" or alan2 == "g" :
                sayı = float(input("Kaç hektometrekareyi kilometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı / 100
                print ("{} hektometrekare {} kilometrekareye eşittir. " .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")
        
        elif alan == "G" or alan == "g" :
            alan2 = input("Kilometrekare birimini hangi birime çevirmek istiyorsunuz? : ")
            if alan2 == "E" or alan2 == "e" :
                print ("KENDİ BİRİMİNİ KENDİ BİRİMİNE ÇEVİREMEZSİN!")
            elif alan2 == "A" or alan2 == "a" :
                sayı = float(input("Kaç kilometrekareyi milimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000000000000
                print ("{} kilometrekare {} milimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "B" or alan2 == "b" :
                sayı = float(input("Kaç kilometrekareyi santimetrekareyi çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10000000000
                print ("{} kilometrekare {} santimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "C" or alan2 == "c" :
                sayı = float(input("Kaç kilometrekareyi desimetrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100000000
                print ("{} kilometrekare {} desimetrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "D" or alan2 == "d" :
                sayı = float(input("Kaç kilometrekareyi metrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 1000000
                print ("{} kilometrekare {} metrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "E" or alan2 == "e" :
                sayı = float(input("Kaç kilometrekareyi dekametrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 10000
                print ("{} kilometrekare {} dekametrekareye eşittir. " .format(sayı,sonuç))
            elif alan2 == "F" or alan2 == "f" :
                sayı = float(input("Kaç kilometrekareyi hektometrekareye çevirmek istiyorsunuz? : "))
                sonuç = sayı * 100
                print ("{} kilometrekare {} hektometrekareye eşittir. " .format(sayı,sonuç))
            else :
                print ("Yanlış seçim yaptınız!")