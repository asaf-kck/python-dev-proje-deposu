import random
kazanc = 0
kasa = 0
print("""BOL ŞANSLAR
          1 ADET KAZI KAZAN 1₺
        ÇIKMAK İÇİN "q" TUŞLAYIN
5 ,6 , 7 , 8 , 9 , 10 ADET "1₺" TUTTURUSANIZ 1₺ KAZANIRSINIZ
5 ,6 , 7 , 8 , 9 , 10 ADET "2₺" TUTTURUSANIZ 2₺ KAZANIRSINIZ
5 ,6 , 7 , 8 , 9 , 10 ADET "5₺" TUTTURUSANIZ 5₺ KAZANIRSINIZ
5 ,6 , 7 , 8 , 9 , 10 ADET "10₺" TUTTURUSANIZ 10₺ KAZANIRSINIZ
5 ,6 , 7 , 8 , 9 , 10 ADET "20₺" TUTTURUSANIZ 20₺ KAZANIRSINIZ
5 ,6 , 7 , 8 , 9 , 10 ADET "100₺" TUTTURUSANIZ 100₺ KAZANIRSINIZ
6 , 7 , 8 , 9 , 10 ADET "5.000₺" TUTTURUSANIZ 5.000₺ KAZANIRSINIZ
6 , 7 , 8 , 9 , 10 ADET "10.000₺" TUTTURUSANIZ 10.000₺ KAZANIRSINIZ
6 , 7 , 8 , 9 , 10 ADET "20.000₺" TUTTURUSANIZ 20.000₺ KAZANIRSINIZ
6 , 7 , 8 , 9 , 10 ADET "100.000₺" TUTTURUSANIZ 100.000₺ KAZANIRSINIZ

          """)
while True:
    oduller1 = ["20₺", "1₺", "2₺", "100₺", "1₺", "10.000₺", "1₺", "5₺", "10₺", "2₺", "5.000₺", "2₺", "2₺", "1₺","100.000₺","2₺", "2₺", "1₺", "1₺", "20.000₺", ]
    oduller2 = ["100.000₺", "100₺", "1₺", "1₺", "2₺", "20₺", "1₺", "1₺", "5₺", "2₺", "20₺", "100₺", "2₺", "1₺", "1₺","20₺", "2₺", "1₺", "1₺", "5.000₺", ]
    oduller3 = ["1₺", "20₺", "2₺", "2₺", "1₺", "10.000₺", "1₺", "5₺", "10₺", "2₺", "5.000₺", "2₺", "2₺", "1₺", "1₺","2₺", "2₺", "20₺","1₺", "20.000₺"]
    oduller4 = ["1₺", "1₺", "100₺", "2₺", "1₺","100.000₺","1₺", "5₺", "10₺", "2₺", "1₺", "2₺","2₺", "1₺", "20₺","2₺", "100₺", "1₺", "1₺", "1₺", ]
    oduller5 = ["1₺", "1₺", "2₺", "2₺", "1₺", "1₺", "10.000₺", "5₺", "10₺", "2₺", "20₺", "2₺", "2₺", "1₺", "1₺","5.000₺", "2₺", "1₺", "1₺", "1₺", ]
    oduller6 = ["100.000₺", "1₺", "2₺", "2₺", "1₺", "1₺", "1₺", "5₺", "10₺", "2₺", "1₺", "5.000₺", "2₺", "1₺", "20₺","2₺", "2₺", "1₺", "100₺", "20.000₺", ]
    oduller7 = ["20₺", "1₺", "100₺", "2₺", "1₺", "10.000₺", "1₺", "5₺", "10₺", "2₺", "5.000₺", "2₺", "20₺", "1₺","100.000₺","2₺", "2₺", "1₺", "1₺", "20.000₺", ]
    oduller8 = ["20₺", "1₺", "2₺", "2₺", "1₺", "10.000₺", "1₺", "5₺", "10₺", "2₺", "5.000₺", "2₺", "2₺", "1₺", "1₺","2₺", "2₺", "1₺", "1₺", "20.000₺", ]
    oduller9 = ["20₺", "1₺", "2₺", "2₺", "1₺", "10.000₺", "1₺", "5₺", "10₺", "2₺", "5.000₺", "2₺", "2₺", "1₺", "20₺","2₺", "2₺", "1₺", "1₺", "20.000₺", ]
    oduller10 = ["20₺", "1₺", "2₺","100.000₺","1₺", "10.000₺", "1₺", "5₺", "10₺", "2₺", "5.000₺", "2₺", "20₺", "1₺", "1₺","2₺", "2₺", "1₺", "100₺", "20.000₺", ]
    para = input("Oynamak İstediginiz Miktar: ")




    if para == "q":
        print("Hoşcakalın, Tekrar Bekleriz ;)")
        print("Kasa:{}₺ Kazanç:{}₺".format(kasa,kazanc))

        break

    else:
        para = int(para)
        kasa += para

        for i in range(0,para):

            sayi1 = random.choice(oduller1)
            sayi2 = random.choice(oduller2)
            sayi3 = random.choice(oduller3)
            sayi4 = random.choice(oduller4)
            sayi5 = random.choice(oduller5)
            sayi6 = random.choice(oduller6)
            sayi7 = random.choice(oduller7)
            sayi8 = random.choice(oduller8)
            sayi9 = random.choice(oduller9)
            sayi10 = random.choice(oduller10)

            print("|",sayi1,"|",sayi2,"|",sayi3,"|",sayi4,"|",sayi5,"|",sayi6,"|",sayi7,"|",sayi8,"|",sayi9,"|",sayi10,"|")
# KAZANAN MİKTAR FONKSİYONU #
            kazanan = [sayi1,sayi2,sayi3,sayi4,sayi5,sayi6,sayi7,sayi8,sayi9,sayi10]
            liste1 = []
            liste2 = []
            liste3 = []
            liste4 = []
            liste5 = []
            liste6 = []
            liste7 = []
            liste8 = []
            liste9 = []
            liste10 = []
            for x in kazanan:


                if x == "1₺":
                    liste1.append(x)
                elif x == "2₺":
                    liste2.append(x)
                elif x == "5₺":
                    liste3.append(x)
                elif x == "10₺":
                    liste4.append(x)
                elif x == "20₺":
                    liste5.append(x)
                elif x == "100₺":
                    liste6.append(x)
                elif x == "5.000₺":
                    liste7.append(x)
                elif x == "10.000₺":
                    liste8.append(x)
                elif x == "20.000₺":
                    liste9.append(x)
                elif x == "100.000₺":
                    liste10.append(x)

            if len(liste1) == 5 or len(liste1) == 6 or len(liste1) == 7 or len(liste1) == 8 or len(liste1) == 9 or len(liste1) == 10:
                kazanc += 1
                print("TEBRİKLER",liste1[1],"KAZANDINIZ")
            elif len(liste2) == 5 or len(liste2) == 6 or len(liste2) == 7 or len(liste2) == 8 or len(liste2) == 9 or len(liste2) == 10:
                kazanc += 2
                print("TEBRİKLER", liste2[1], "KAZANDINIZ")
            elif len(liste3) == 5 or len(liste3) == 6 or len(liste3) == 7 or len(liste3) == 8 or len(liste3) == 9 or len(liste3) == 10:
                kazanc += 5
                print("TEBRİKLER", liste3[1], "KAZANDINIZ")
            elif len(liste4) == 5 or len(liste4) == 6 or len(liste4) == 7 or len(liste4) == 8 or len(liste4) == 9 or len(liste4) == 10:
                kazanc += 10
                print("TEBRİKLER", liste4[1], "KAZANDINIZ")
            elif len(liste5) == 5 or len(liste5) == 6 or len(liste5) == 7 or len(liste5) == 8 or len(liste5) == 9 or len(liste5) == 10:
                kazanc += 20
                print("TEBRİKLER", liste5[1], "KAZANDINIZ")
            elif len(liste6) == 6 or len(liste6) == 7 or len(liste6) == 8 or len(liste6) == 9 or len(liste6) == 10:
                kazanc += 100
                print("TEBRİKLER", liste6[1], "KAZANDINIZ")
            elif len(liste7) == 6 or len(liste7) == 7 or len(liste7) == 8 or len(liste7) == 9 or len(liste7) == 10:
                kazanc += 5000
                print("TEBRİKLER", liste7[1], "KAZANDINIZ")
            elif len(liste8) == 6 or len(liste8) == 7 or len(liste8) == 8 or len(liste8) == 9 or len(liste8) == 10:
                kazanc += 10000
                print("TEBRİKLER", liste8[1], "KAZANDINIZ")
            elif len(liste9) == 6 or len(liste9) == 7 or len(liste9) == 8 or len(liste9) == 9 or len(liste9) == 10:
                kazanc += 20000
                print("TEBRİKLER", liste9[1], "KAZANDINIZ")
            elif len(liste10) == 6 or len(liste10) == 7 or len(liste10) == 8 or len(liste10) == 9 or len(liste10) == 10:
                kazanc += 100000
                print("TEBRİKLER", liste10[1], "KAZANDINIZ")