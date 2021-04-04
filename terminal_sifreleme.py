
while True:
   
    q_klavye_düzeni = "qwertyuıopğüasdfghjklşi,zxcvbnmöç. "
    ş_klavye_düzeni = """*!#+$%&/{([)]=}?*\Q@"é;:.,<>|~asdf """
    print("1)Şifre Oluşturmak İstiyorum")
    print("2)Var Olan Şifreyi Çözmek İstiyorum")
    print("3)Programdan Çıkmak İstiyorum")
    seçim = int(input("Seçiniz: "))
    import os
    os.system("cls")
    
    if seçim == 1:
        metin=input("Şifrelenmesini istediğiniz metni girin: ")
        çeviri_tablosu = str.maketrans(q_klavye_düzeni, ş_klavye_düzeni)
        print("Şifrelenmiş Metin:",metin.translate(çeviri_tablosu))
        print("\n"*2)
        
    elif seçim == 2:
        metin1=input("Çözülmesini istediğiniz şifreyi girin: ")
        çeviri_tablosu = str.maketrans(ş_klavye_düzeni, q_klavye_düzeni)
        print("Çözülmüş Şifre:",metin1.translate(çeviri_tablosu))
        print("\n"*2)

    elif seçim == 3:
        exit()

    else:
        import os
        os.system("cls")
        print("Az Önce Hatalı Bir Seçim Yaptınız Lüften Yeniden Deneyiniz.","\n")