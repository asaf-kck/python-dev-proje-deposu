print ("""
===============================
Sanal Marketimize Hoşgeldiniz.
===============================
ÜRÜN LİSTESİ VE FİYATLAR :
[1]Et ve Süt Ürünleri:
    - kırmızı et (kilo : 60₺)
    - tavuk (kilo : 40₺)
    - süt (litre : 4₺)
    - peynir (kilo : 15₺)
    - yoğurt (kutu : 10₺)
    - salam (kilo : 20₺)
    - sucuk (klio : 30₺)
    - sosis (kilo : 80₺)
    - pastırma (kilo : 100₺)
[2]Temel Gıdalar :
    - makarna (paket : 3₺)
    - un (kilo : 2₺)
    - yağlar:
        + zeytinyağı (litre : 22₺)
        + ayçiçek yağı (litre : 12₺)
        + tereyağ (kilo : 50₺)
    - şeker (kilo : 7₺)
    - bakliyat:
        + pirinç (kilo : 10₺)
        + yeşil mercimek (kilo : 8₺)
        + kırmızı mercimek (kilo : 7₺)
        + nohut (kilo : 12)
        + bulgur (kilo : 6.5)
        + kuru fasulye (kilo : 14₺)
[3]Kahvaltılıklar :
    - yumurta (adet : 1₺)
    - reçel (kavanoz : 20₺)
    - pekmez (kavanoz : 12₺)
    - tahin (kavanoz : 15₺)
    - mısır gevreği (paket : 10₺)
    - helva (kilo : 26₺)
[4]Atıştırmalıklar :
    - çikolata (adet : 3.5₺)
    - kraker (paket : 1.5₺)
    - şeker (adet : 0.5₺)
    - cips (paket : 5₺)
    - kuruyemiş (kilo : 40₺)
    - dondurma (adet : 4.5₺)
[5]İçecekler :
    Kutu İçecekler  :
        - kola (kutu : 3)
        - gazoz (kutu :3)
        - fanta (kutu : 3)
        - buzlu çay (kutu : 3)
        - soğuk kahve (kutu : 7)
    Meyve Suları :
        - vişneli (paket : 2)
        - kayısılı (paket : 2)
        - şeftalili (paket :2)
        - karışık (paket :2)
[6]Temizlik Malzemeleri :
    - çamaşır deterjanı (litre : 27.5₺)
    - bulaşık deterjanı (litre : 10.5₺)
""")

sepet = []
fiyat = []
toplamfiyat = 0


while True :
    tür = str(input("Hangi tür ürün istiyorsunuz? Listedeki rakamlarla belirtiniz. 0'a basarak çıkıp fiyat bilgisini öğrenebilirsiniz. : "))

    if tür == ("Et ve Süt Ürünleri"):
        tercih = str(input("Hangi ürünü istiyorsunuz? : "))
        if tercih == ("kırmızı et"):
            A = ("kırmızı et")
            sepet.append(A)
            kilo = int(input("Kaç kg kırmızı et istiyorsunuz?: "))
            ürünfiyatı = kilo*60
            fiyat.append(ürünfiyatı)
            toplamfiyat += ürünfiyatı
        elif tercih == ("tavuk"):
            B = ("tavuk")
            sepet.append(B)
            kilo = int(input("Kaç kg tavuk istiyorsunuz?: "))
            ürünfiyatı2 = kilo*40
            fiyat.append(ürünfiyatı2)
            toplamfiyat += ürünfiyatı2
        elif tercih == ("süt"):
            C = ("süt")
            sepet.append(C)
            kilo = int(input("Kaç litre süt istiyorsunuz?: "))
            ürünfiyatı3 = kilo*4
            fiyat.append(ürünfiyatı3)
            toplamfiyat += ürünfiyatı3
        elif tercih == ("peynir"):
            D = ("peynir")
            sepet.append(D)
            kilo = int(input("Kaç kg peynir istiyorsunuz?: "))
            ürünfiyatı4 = kilo*15
            fiyat.append(ürünfiyatı4)
            toplamfiyat += ürünfiyatı4
        elif tercih == ("yoğurt"):
            E = ("yoğurt")
            sepet.append(E)
            kilo = int(input("Kaç kutu yoğurt istiyorsunuz?: "))
            ürünfiyatı5 = kilo*10
            fiyat.append(ürünfiyatı5)
            toplamfiyat += ürünfiyatı5
        elif tercih == ("salam"):
            F = ("salam")
            sepet.append(F)
            kilo = int(input("Kaç kg salam istiyorsunuz?: "))
            ürünfiyatı6 = kilo*20
            fiyat.append(ürünfiyatı6)
            toplamfiyat += ürünfiyatı6
        elif tercih == ("sosis"):
            G = ("sosis")
            sepet.append(G)
            kilo = int(input("Kaç kg sosis istiyorsunuz?: "))
            ürünfiyatı7 = kilo*30
            fiyat.append(ürünfiyatı7)
            toplamfiyat += ürünfiyatı7
        elif tercih == ("sucuk"):
            Ğ = ("sucuk")
            sepet.append(Ğ)
            kilo = int(input("Kaç kg sucuk istiyorsunuz?: "))
            ürünfiyatı8 = kilo*80
            fiyat.append(ürünfiyatı8)
            toplamfiyat += ürünfiyatı8
        elif tercih == ("pastırma"):
            H = ("pastırma")
            sepet.append(H)
            kilo = int(input("Kaç kg pastırma istiyorsunuz?: "))
            ürünfiyatı9 = kilo*100
            fiyat.append(ürünfiyatı9)
            toplamfiyat += ürünfiyatı9
        else :
            print("Yanlış seçim yaptınız!")
    elif tür == ("1"):
        tercih = str(input("Hangi ürünü istiyorsunuz? : "))
        if tercih == ("kırmızı et"):
            A = ("kırmızı et")
            sepet.append(A)
            kilo = int(input("Kaç kg kırmızı et istiyorsunuz?: "))
            ürünfiyatı = kilo*60
            fiyat.append(ürünfiyatı)
            toplamfiyat += ürünfiyatı
        elif tercih == ("tavuk"):
            B = ("tavuk")
            sepet.append(B)
            kilo = int(input("Kaç kg tavuk istiyorsunuz?: "))
            ürünfiyatı2 = kilo*40
            fiyat.append(ürünfiyatı2)
            toplamfiyat += ürünfiyatı2
        elif tercih == ("süt"):
            C = ("süt")
            sepet.append(C)
            kilo = int(input("Kaç litre süt istiyorsunuz?: "))
            ürünfiyatı3 = kilo*4
            fiyat.append(ürünfiyatı3)
            toplamfiyat += ürünfiyatı3
        elif tercih == ("peynir"):
            D = ("peynir")
            sepet.append(D)
            kilo = int(input("Kaç kg peynir istiyorsunuz?: "))
            ürünfiyatı4 = kilo*15
            fiyat.append(ürünfiyatı4)
            toplamfiyat += ürünfiyatı4
        elif tercih == ("yoğurt"):
            E = ("yoğurt")
            sepet.append(E)
            kilo = int(input("Kaç kutu yoğurt istiyorsunuz?: "))
            ürünfiyatı5 = kilo*10
            fiyat.append(ürünfiyatı5)
            toplamfiyat += ürünfiyatı5
        elif tercih == ("salam"):
            F = ("salam")
            sepet.append(F)
            kilo = int(input("Kaç kg salam istiyorsunuz?: "))
            ürünfiyatı6 = kilo*20
            fiyat.append(ürünfiyatı6)
            toplamfiyat += ürünfiyatı6
        elif tercih == ("sosis"):
            G = ("sosis")
            sepet.append(G)
            kilo = int(input("Kaç kg sosis istiyorsunuz?: "))
            ürünfiyatı7 = kilo*30
            fiyat.append(ürünfiyatı7)
            toplamfiyat += ürünfiyatı7
        elif tercih == ("sucuk"):
            Ğ = ("sucuk")
            sepet.append(Ğ)
            kilo = int(input("Kaç kg sucuk istiyorsunuz?: "))
            ürünfiyatı8 = kilo*80
            fiyat.append(ürünfiyatı8)
            toplamfiyat += ürünfiyatı8
        elif tercih == ("pastırma"):
            H = ("pastırma")
            sepet.append(H)
            kilo = int(input("Kaç kg pastırma istiyorsunuz?: "))
            ürünfiyatı9 = kilo*100
            fiyat.append(ürünfiyatı9)
            toplamfiyat += ürünfiyatı9
        else :
            print("Yanlış seçim yaptınız!")
    elif tür == ("Temel Gıdalar") :
        tercih2 = str(input("Hangi ürünü istiyorsunuz? : "))
        if tercih2 == ("makarna") :
            I = ("makarna")
            sepet.append(I)
            kilo = int(input("Kaç paket makarna istiyorsunuz? : "))
            ürünfiyatı10 = kilo*3
            fiyat.append(ürünfiyatı10)
            toplamfiyat += ürünfiyatı10
        elif tercih2 == ("yağlar") :
            yağtürü = str(input("Hangi tür yağ istiyorsunuz? : "))
            if yağtürü == ("zeytinyağı"):
                İ = ("zeytinyağı")
                sepet.append(İ)
                kilo = int(input("Kaç litre zeytinyağı istiyorsunuz? : "))
                ürünfiyatı11 = kilo*22
                fiyat.append(ürünfiyatı11)
                toplamfiyat += ürünfiyatı11
            elif yağtürü == ("ayçiçek yağı"):
                J = ("ayçiçek yağı")
                sepet.append(J)
                kilo = int(input("Kaç litre ayçiçek yağı istiyorsunuz? : "))
                ürünfiyatı12 = kilo*12
                fiyat.append(ürünfiyatı12)
                toplamfiyat += ürünfiyatı12
            elif yağtürü == ("tereyağ"):
                K = ("tereyağ")
                sepet.append(K)
                kilo = int(input("Kaç kg tereyağ istiyorsunuz? : "))
                ürünfiyatı13 = kilo*50
                fiyat.append(ürünfiyatı13)
                toplamfiyat += ürünfiyatı13
            else :
                print ("Yanlış seçim yaptınız!")
        elif tercih2 == ("un") :
            L = ("un")
            sepet.append(L)
            kilo = int(input("Kaç kg un istiyorsunuz? : "))
            ürünfiyatı14 = kilo*2
            fiyat.append(ürünfiyatı14)
            toplamfiyat += ürünfiyatı14
        elif tercih2 == ("şeker") :
            M = ("şeker")
            sepet.append(M)
            kilo = int(input("Kaç kilo şeker istiyorsunuz? : "))
            ürünfiyatı15 = kilo*7
            fiyat.append(ürünfiyatı15)
            toplamfiyat += ürünfiyatı15
        elif tercih2 == ("bakliyat") :
            bakliyat = str(input("Hangi tür bakliyat istiyorsunuz? : "))
            if bakliyat == ("pirinç") :
                N = ("pirinç")
                sepet.append(N)
                kilo = int(input("Kaç kg pirinç istiyorsunuz? : "))
                ürünfiyatı16 = kilo*10
                fiyat.append(ürünfiyatı16)
                toplamfiyat += ürünfiyatı16
            elif bakliyat == ("yeşil mercimek") :
                O = ("yeşil mercimek")
                sepet.append(O)
                kilo = int(input("Kaç kg yeşil mercimek istiyorsunuz? : "))
                ürünfiyatı17 = kilo*8
                fiyat.append(ürünfiyatı17)
                toplamfiyat += ürünfiyatı17
            elif bakliyat == ("kırmızı mercimek"):
                Ö = ("kırmızı mercimek")
                sepet.append(Ö)
                kilo = int(input("Kaç kg kırmızı mercimek istiyorsunuz? : "))
                ürünfiyatı18 = kilo*7
                fiyat.append(ürünfiyatı18)
                toplamfiyat += ürünfiyatı18
            elif bakliyat == ("nohut"):
                P = ("nohut")
                sepet.append(P)
                kilo = int(input("Kaç kg nohut istiyorsunuz? : "))
                ürünfiyatı18 = kilo*12
                fiyat.append(ürünfiyatı18)
                toplamfiyat += ürünfiyatı18
            elif bakliyat == ("bulgur"):
                R = ("bulgur")
                sepet.append(R)
                kilo = int(input("Kaç kg bulgur istiyorsunuz? : "))
                ürünfiyatı19 = kilo*6.5
                fiyat.append(ürünfiyatı19)
                toplamfiyat += ürünfiyatı19
            elif bakliyat == ("kuru fasulye"):
                S = ("kuru fasulye")
                sepet.append(S)
                kilo = int(input("Kaç kg kuru fasulye istiyorsunuz? : "))
                ürünfiyatı20 = kilo*14
                fiyat.append(ürünfiyatı20)
                toplamfiyat += ürünfiyatı20
            else :
                print ("Yanlış seçim yaptınız!")
    elif tür == ("2") :
        tercih2 = str(input("Hangi ürünü istiyorsunuz? : "))
        if tercih2 == ("makarna") :
            I = ("makarna")
            sepet.append(I)
            kilo = int(input("Kaç paket makarna istiyorsunuz? : "))
            ürünfiyatı10 = kilo*3
            fiyat.append(ürünfiyatı10)
            toplamfiyat += ürünfiyatı10
        elif tercih2 == ("yağlar") :
            yağtürü = str(input("Hangi tür yağ istiyorsunuz? : "))
            if yağtürü == ("zeytinyağı"):
                İ = ("zeytinyağı")
                sepet.append(İ)
                kilo = int(input("Kaç litre zeytinyağı istiyorsunuz? : "))
                ürünfiyatı11 = kilo*22
                fiyat.append(ürünfiyatı11)
                toplamfiyat += ürünfiyatı11
            elif yağtürü == ("ayçiçek yağı"):
                J = ("ayçiçek yağı")
                sepet.append(J)
                kilo = int(input("Kaç litre ayçiçek yağı istiyorsunuz? : "))
                ürünfiyatı12 = kilo*12
                fiyat.append(ürünfiyatı12)
                toplamfiyat += ürünfiyatı12
            elif yağtürü == ("tereyağ"):
                K = ("tereyağ")
                sepet.append(K)
                kilo = int(input("Kaç kg tereyağ istiyorsunuz? : "))
                ürünfiyatı13 = kilo*50
                fiyat.append(ürünfiyatı13)
                toplamfiyat += ürünfiyatı13
            else :
                print ("Yanlış seçim yaptınız!")
        elif tercih2 == ("un") :
            L = ("un")
            sepet.append(L)
            kilo = int(input("Kaç kg un istiyorsunuz? : "))
            ürünfiyatı14 = kilo*2
            fiyat.append(ürünfiyatı14)
            toplamfiyat += ürünfiyatı14
        elif tercih2 == ("şeker") :
            M = ("şeker")
            sepet.append(M)
            kilo = int(input("Kaç kilo şeker istiyorsunuz? : "))
            ürünfiyatı15 = kilo*7
            fiyat.append(ürünfiyatı15)
            toplamfiyat += ürünfiyatı15
        elif tercih2 == ("bakliyat") :
            bakliyat = str(input("Hangi tür bakliyat istiyorsunuz? : "))
            if bakliyat == ("pirinç") :
                N = ("pirinç")
                sepet.append(N)
                kilo = int(input("Kaç kg pirinç istiyorsunuz? : "))
                ürünfiyatı16 = kilo*10
                fiyat.append(ürünfiyatı16)
                toplamfiyat += ürünfiyatı16
            elif bakliyat == ("yeşil mercimek") :
                O = ("yeşil mercimek")
                sepet.append(O)
                kilo = int(input("Kaç kg yeşil mercimek istiyorsunuz? : "))
                ürünfiyatı17 = kilo*8
                fiyat.append(ürünfiyatı17)
                toplamfiyat += ürünfiyatı17
            elif bakliyat == ("kırmızı mercimek"):
                Ö = ("kırmızı mercimek")
                sepet.append(Ö)
                kilo = int(input("Kaç kg kırmızı mercimek istiyorsunuz? : "))
                ürünfiyatı18 = kilo*7
                fiyat.append(ürünfiyatı18)
                toplamfiyat += ürünfiyatı18
            elif bakliyat == ("nohut"):
                P = ("nohut")
                sepet.append(P)
                kilo = int(input("Kaç kg nohut istiyorsunuz? : "))
                ürünfiyatı18 = kilo*12
                fiyat.append(ürünfiyatı18)
                toplamfiyat += ürünfiyatı18
            elif bakliyat == ("bulgur"):
                R = ("bulgur")
                sepet.append(R)
                kilo = int(input("Kaç kg bulgur istiyorsunuz? : "))
                ürünfiyatı19 = kilo*6.5
                fiyat.append(ürünfiyatı19)
                toplamfiyat += ürünfiyatı19
            elif bakliyat == ("kuru fasulye"):
                S = ("kuru fasulye")
                sepet.append(S)
                kilo = int(input("Kaç kg kuru fasulye istiyorsunuz? : "))
                ürünfiyatı20 = kilo*14
                fiyat.append(ürünfiyatı20)
                toplamfiyat += ürünfiyatı20
            else :
                print ("Yanlış seçim yaptınız!")
    elif tür == ("Kahvaltılıklar") :
        tercih3 = str(input("Hangi ürünü istiyorsunuz? : "))
        if tercih3 == ("yumurta"):
            Ş = ("yumurta")
            sepet.append(Ş)
            adet = int(input("Kaç adet yumurta istiyorsunuz?: "))
            ürünfiyatı21 = kilo*1
            fiyat.append(ürünfiyatı21)
            toplamfiyat += ürünfiyatı21
        elif tercih3 == ("reçel"):
            T = ("reçel")
            sepet.append(T)
            kilo = int(input("Kaç kavanoz reçel istiyorsunuz?: "))
            ürünfiyatı22 = kilo*20
            fiyat.append(ürünfiyatı22)
            toplamfiyat += ürünfiyatı22
        elif tercih3 == ("pekmez"):
            U = ("pekmez")
            sepet.append(U)
            kilo = int(input("Kaç kavanoz pekmez istiyorsunuz?: "))
            ürünfiyatı23 = kilo*12
            fiyat.append(ürünfiyatı23)
            toplamfiyat += ürünfiyatı23
        elif tercih3 == ("tahin"):
            Ü = ("tahin")
            sepet.append(Ü)
            kilo = int(input("Kaç kavanoz tahin istiyorsunuz?: "))
            ürünfiyatı24 = kilo*15
            fiyat.append(ürünfiyatı24)
            toplamfiyat += ürünfiyatı24
        elif tercih3 == ("mısır gevreği"):
            V = ("mısır gevreği")
            sepet.append(V)
            kilo = int(input("Kaç paket mısır gevreği istiyorsunuz?: "))
            ürünfiyatı25 = kilo*10
            fiyat.append(ürünfiyatı25)
            toplamfiyat += ürünfiyatı25       
        elif tercih3 == ("helva"):
            Y = ("helva")
            sepet.append(Y)
            kilo = int(input("Kaç kg helva istiyorsunuz?: "))
            ürünfiyatı26 = kilo*26
            fiyat.append(ürünfiyatı26)
            toplamfiyat += ürünfiyatı26
        else :
            print ("Yanlış seçim yaptınız!")
    elif tür == ("3") :
        tercih3 = str(input("Hangi ürünü istiyorsunuz? : "))
        if tercih3 == ("yumurta"):
            Ş = ("yumurta")
            sepet.append(Ş)
            adet = int(input("Kaç adet yumurta istiyorsunuz?: "))
            ürünfiyatı21 = kilo*1
            fiyat.append(ürünfiyatı21)
            toplamfiyat += ürünfiyatı21
        elif tercih3 == ("reçel"):
            T = ("reçel")
            sepet.append(T)
            kilo = int(input("Kaç kavanoz reçel istiyorsunuz?: "))
            ürünfiyatı22 = kilo*20
            fiyat.append(ürünfiyatı22)
            toplamfiyat += ürünfiyatı22
        elif tercih3 == ("pekmez"):
            U = ("pekmez")
            sepet.append(U)
            kilo = int(input("Kaç kavanoz pekmez istiyorsunuz?: "))
            ürünfiyatı23 = kilo*12
            fiyat.append(ürünfiyatı23)
            toplamfiyat += ürünfiyatı23
        elif tercih3 == ("tahin"):
            Ü = ("tahin")
            sepet.append(Ü)
            kilo = int(input("Kaç kavanoz tahin istiyorsunuz?: "))
            ürünfiyatı24 = kilo*15
            fiyat.append(ürünfiyatı24)
            toplamfiyat += ürünfiyatı24
        elif tercih3 == ("mısır gevreği"):
            V = ("mısır gevreği")
            sepet.append(V)
            kilo = int(input("Kaç paket mısır gevreği istiyorsunuz?: "))
            ürünfiyatı25 = kilo*10
            fiyat.append(ürünfiyatı25)
            toplamfiyat += ürünfiyatı25       
        elif tercih3 == ("helva"):
            Y = ("helva")
            sepet.append(Y)
            kilo = int(input("Kaç kg helva istiyorsunuz?: "))
            ürünfiyatı26 = kilo*26
            fiyat.append(ürünfiyatı26)
            toplamfiyat += ürünfiyatı26
        else :
            print ("Yanlış seçim yaptınız!")
    elif tür == ("Atıştırmalıklar") :
        tercih4 = str(input("Hangi ürünü istiyorsunuz? : "))
        if tercih4 == ("çikolata"):
            Z = ("çikolata")
            sepet.append(Z)
            kilo = int(input("Kaç  adet çikolata istiyorsunuz?: "))
            ürünfiyatı27 = kilo*3.5
            fiyat.append(ürünfiyatı27)
            toplamfiyat += ürünfiyatı27
        elif tercih4 == ("kraker"):
            AA = ("kraker")
            sepet.append(AA)
            kilo = int(input("Kaç paket kraker istiyorsunuz?: "))
            ürünfiyatı28 = kilo*1.5
            fiyat.append(ürünfiyatı28)
            toplamfiyat += ürünfiyatı28
        elif tercih4 == ("şeker"):
            AB = ("şeker")
            sepet.append(AB)
            kilo = int(input("Kaç adet şeker istiyorsunuz?: "))
            ürünfiyatı29 = kilo*0.5
            fiyat.append(ürünfiyatı29)
            toplamfiyat += ürünfiyatı29
        elif tercih4 == ("cips"):
            AC = ("cips")
            sepet.append(AC)
            kilo = int(input("Kaç paket cips istiyorsunuz?: "))
            ürünfiyatı30 = kilo*5
            fiyat.append(ürünfiyatı30)
            toplamfiyat += ürünfiyatı30
        elif tercih4 == ("kuruyemiş"):
            AD = ("kuruyemiş")
            sepet.append(AD)
            kilo = int(input("Kaç kg kuruyemiş istiyorsunuz?: "))
            ürünfiyatı31 = kilo*40
            fiyat.append(ürünfiyatı31)
            toplamfiyat += ürünfiyatı31
        elif tercih4 == ("dondurma"):
            AE = ("dondurma")
            sepet.append(AE)
            kilo = int(input("Kaç adet dondurma istiyorsunuz?: "))
            ürünfiyatı32 = kilo*4.5
            fiyat.append(ürünfiyatı32)
            toplamfiyat += ürünfiyatı32
        else :
            print("Yanlış seçim yaptınız!")
    elif tür == ("4") :
        tercih4 = str(input("Hangi ürünü istiyorsunuz? : "))
        if tercih4 == ("çikolata"):
            Z = ("çikolata")
            sepet.append(Z)
            kilo = int(input("Kaç  adet çikolata istiyorsunuz?: "))
            ürünfiyatı27 = kilo*3.5
            fiyat.append(ürünfiyatı27)
            toplamfiyat += ürünfiyatı27
        elif tercih4 == ("kraker"):
            AA = ("kraker")
            sepet.append(AA)
            kilo = int(input("Kaç paket kraker istiyorsunuz?: "))
            ürünfiyatı28 = kilo*1.5
            fiyat.append(ürünfiyatı28)
            toplamfiyat += ürünfiyatı28
        elif tercih4 == ("şeker"):
            AB = ("şeker")
            sepet.append(AB)
            kilo = int(input("Kaç adet şeker istiyorsunuz?: "))
            ürünfiyatı29 = kilo*0.5
            fiyat.append(ürünfiyatı29)
            toplamfiyat += ürünfiyatı29
        elif tercih4 == ("cips"):
            AC = ("cips")
            sepet.append(AC)
            kilo = int(input("Kaç paket cips istiyorsunuz?: "))
            ürünfiyatı30 = kilo*5
            fiyat.append(ürünfiyatı30)
            toplamfiyat += ürünfiyatı30
        elif tercih4 == ("kuruyemiş"):
            AD = ("kuruyemiş")
            sepet.append(AD)
            kilo = int(input("Kaç kg kuruyemiş istiyorsunuz?: "))
            ürünfiyatı31 = kilo*40
            fiyat.append(ürünfiyatı31)
            toplamfiyat += ürünfiyatı31
        elif tercih4 == ("dondurma"):
            AE = ("dondurma")
            sepet.append(AE)
            kilo = int(input("Kaç adet dondurma istiyorsunuz?: "))
            ürünfiyatı32 = kilo*4.5
            fiyat.append(ürünfiyatı32)
            toplamfiyat += ürünfiyatı32
        else :
            print("Yanlış seçim yaptınız!")
    elif tür == ("İçecekler") :
        tercih5 = str(input("Hangi  tür içecek istiyorsunuz?: "))
        if tercih5 == ("Kutu İçecekler") :
            içecektürü = str(input("Hangi tür kutu içecek istiyorsunuz? : "))
            if içecektürü == ("kola"):
                AF = ("kola")
                sepet.append(AF)
                kilo = int(input("Kaç kutu kola istiyorsunuz? : "))
                ürünfiyatı33 = kilo*3
                fiyat.append(ürünfiyatı33)
                toplamfiyat += ürünfiyatı33
            elif içecektürü == ("gazoz"):
                AG = ("gazoz")
                sepet.append(AG)
                kilo = int(input("Kaç kutu gazoz istiyorsunuz? : "))
                ürünfiyatı34 = kilo*3
                fiyat.append(ürünfiyatı34)
                toplamfiyat += ürünfiyatı34
            elif içecektürü == ("fanta"):
                AĞ = ("fanta")
                sepet.append(AĞ)
                kilo = int(input("Kaç kutu fanta istiyorsunuz? : "))
                ürünfiyatı35 = kilo*3
                fiyat.append(ürünfiyatı35)
                toplamfiyat += ürünfiyatı35
            elif içecektürü == ("buzlu çay"):
                AH = ("buzlu çay")
                sepet.append(AH)
                kilo = int(input("Kaç kutu buzlu çay istiyorsunuz? : "))
                ürünfiyatı36 = kilo*3
                fiyat.append(ürünfiyatı36)
                toplamfiyat += ürünfiyatı36
            elif içecektürü == ("soğuk kahve"):
                AI = ("soğuk kahve")
                sepet.append(AI)
                kilo = int(input("Kaç kutu soğuk kahve istiyorsunuz? : "))
                ürünfiyatı37 = kilo*7
                fiyat.append(ürünfiyatı37)
                toplamfiyat += ürünfiyatı37
            else :
                print("Yanlış seçim Yaptınız!")
        elif tercih5 == ("Meyve Suları"):
            içecektürü = str(input("Hangi tür meyve suyu istiyorsunuz? : "))
            if içecektürü == ("vişneli"):
                Aİ = ("vişneli meyve suyu")
                sepet.append(Aİ)
                kilo = int(input("Kaç paket vişneli meyve suyu istiyorsunuz? : "))
                ürünfiyatı38 = kilo*2
                fiyat.append(ürünfiyatı38)
                toplamfiyat += ürünfiyatı38
            elif içecektürü == ("kayısılı"):
                AJ = ("kayısılı meyve suyu")
                sepet.append(AJ)
                kilo = int(input("Kaç paket kayısılı meyve suyu istiyorsunuz? : "))
                ürünfiyatı39 = kilo*2
                fiyat.append(ürünfiyatı39)
                toplamfiyat += ürünfiyatı39
            elif içecektürü == ("şeftalili"):
                AK = ("şeftalili meyve suyu")
                sepet.append(AK)
                kilo = int(input("Kaç paket şeftalili meyve suyu istiyorsunuz? : "))
                ürünfiyatı40 = kilo*2
                fiyat.append(ürünfiyatı40)
                toplamfiyat += ürünfiyatı40
            elif içecektürü == ("karışık"):
                AL = ("karışık meyve suyu")
                sepet.append(AL)
                kilo = int(input("Kaç paket karışık meyve suyu istiyorsunuz? : "))
                ürünfiyatı41 = kilo*2
                fiyat.append(ürünfiyatı41)
                toplamfiyat += ürünfiyatı41
            else :
                print ("Yanlış seçim yaptınız!")
    elif tür == ("5") :
        tercih5 = str(input("Hangi  tür içecek istiyorsunuz?: "))
        if tercih5 == ("Kutu İçecekler") :
            içecektürü = str(input("Hangi tür kutu içecek istiyorsunuz? : "))
            if içecektürü == ("kola"):
                AF = ("kola")
                sepet.append(AF)
                kilo = int(input("Kaç kutu kola istiyorsunuz? : "))
                ürünfiyatı33 = kilo*3
                fiyat.append(ürünfiyatı33)
                toplamfiyat += ürünfiyatı33
            elif içecektürü == ("gazoz"):
                AG = ("gazoz")
                sepet.append(AG)
                kilo = int(input("Kaç kutu gazoz istiyorsunuz? : "))
                ürünfiyatı34 = kilo*3
                fiyat.append(ürünfiyatı34)
                toplamfiyat += ürünfiyatı34
            elif içecektürü == ("fanta"):
                AĞ = ("fanta")
                sepet.append(AĞ)
                kilo = int(input("Kaç kutu fanta istiyorsunuz? : "))
                ürünfiyatı35 = kilo*3
                fiyat.append(ürünfiyatı35)
                toplamfiyat += ürünfiyatı35
            elif içecektürü == ("buzlu çay"):
                AH = ("buzlu çay")
                sepet.append(AH)
                kilo = int(input("Kaç kutu buzlu çay istiyorsunuz? : "))
                ürünfiyatı36 = kilo*3
                fiyat.append(ürünfiyatı36)
                toplamfiyat += ürünfiyatı36
            elif içecektürü == ("soğuk kahve"):
                AI = ("soğuk kahve")
                sepet.append(AI)
                kilo = int(input("Kaç kutu soğuk kahve istiyorsunuz? : "))
                ürünfiyatı37 = kilo*7
                fiyat.append(ürünfiyatı37)
                toplamfiyat += ürünfiyatı37
            else :
                print("Yanlış seçim Yaptınız!")
        elif tercih5 == ("Meyve Suları"):
            içecektürü = str(input("Hangi tür meyve suyu istiyorsunuz? : "))
            if içecektürü == ("vişneli"):
                Aİ = ("vişneli meyve suyu")
                sepet.append(Aİ)
                kilo = int(input("Kaç paket vişneli meyve suyu istiyorsunuz? : "))
                ürünfiyatı38 = kilo*2
                fiyat.append(ürünfiyatı38)
                toplamfiyat += ürünfiyatı38
            elif içecektürü == ("kayısılı"):
                AJ = ("kayısılı meyve suyu")
                sepet.append(AJ)
                kilo = int(input("Kaç paket kayısılı meyve suyu istiyorsunuz? : "))
                ürünfiyatı39 = kilo*2
                fiyat.append(ürünfiyatı39)
                toplamfiyat += ürünfiyatı39
            elif içecektürü == ("şeftalili"):
                AK = ("şeftalili meyve suyu")
                sepet.append(AK)
                kilo = int(input("Kaç paket şeftalili meyve suyu istiyorsunuz? : "))
                ürünfiyatı40 = kilo*2
                fiyat.append(ürünfiyatı40)
                toplamfiyat += ürünfiyatı40
            elif içecektürü == ("karışık"):
                AL = ("karışık meyve suyu")
                sepet.append(AL)
                kilo = int(input("Kaç paket karışık meyve suyu istiyorsunuz? : "))
                ürünfiyatı41 = kilo*2
                fiyat.append(ürünfiyatı41)
                toplamfiyat += ürünfiyatı41
            else :
                print ("Yanlış seçim yaptınız!")
    elif tür == ("Temizlik Malzemeleri") :
        tercih6 = str(input("Hangi ürünü istiyorsunuz? : "))
        if tercih6 == ("çamaşır deterjanı"):
            AM = ("çamaşır deterjanı")
            sepet.append(AM)
            kilo = int(input("Kaç litre çamaşır deterjanı istiyorsunuz?: "))
            ürünfiyatı42 = kilo*27.5
            fiyat.append(ürünfiyatı42)
            toplamfiyat += ürünfiyatı42
        elif tercih6 == ("bulaşık deterjanı"):
            AN = ("bulaşık deterjanı")
            sepet.append(AN)
            kilo = int(input("Kaç litre bulaşık deterjanı istiyorsunuz?: "))
            ürünfiyatı43 = kilo*10.5
            fiyat.append(ürünfiyatı43)
            toplamfiyat += ürünfiyatı43
        else :
            print ("Yanlış seçim yaptınız!")
    elif tür == ("6") :
        tercih6 = str(input("Hangi ürünü istiyorsunuz? : "))
        if tercih6 == ("çamaşır deterjanı"):
            AM = ("çamaşır deterjanı")
            sepet.append(AM)
            kilo = int(input("Kaç litre çamaşır deterjanı istiyorsunuz?: "))
            ürünfiyatı42 = kilo*27.5
            fiyat.append(ürünfiyatı42)
            toplamfiyat += ürünfiyatı42
        elif tercih6 == ("bulaşık deterjanı"):
            AN = ("bulaşık deterjanı")
            sepet.append(AN)
            kilo = int(input("Kaç litre bulaşık deterjanı istiyorsunuz?: "))
            ürünfiyatı43 = kilo*10.5
            fiyat.append(ürünfiyatı43)
            toplamfiyat += ürünfiyatı43
        else :
            print ("Yanlış seçim yaptınız!")

    elif tür == ("0") :
        print ("Aldığınız ürünler : " ,sepet)
        print ("Aldığınız ürünlerin sırayla fiyatları : " ,fiyat)
        print ("Aldığınız ürünlerin toplam fiyatı : " , toplamfiyat)
        break

    else :
        print ("Yanlış seçim yaptınız!")

while True:
    pass