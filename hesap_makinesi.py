islem=input("İşlemi Giriniz:")
sayi1=int(input("Sayi1:"))
sayi2=int(input("Sayi2:"))
if islem=="+":
    sonuc=int(sayi1)+int(sayi2)
    print("Sonuc:",str(sonuc))
elif islem=="-":
    sonuc=int(sayi1)-int(sayi2)
    print("Sonuc:",str(sonuc))
elif islem=="*":
    sonuc=int(sayi1)*int(sayi2)
    print("Sonuc:",str(sonuc))
elif islem=="/":
    sonuc=int(sayi1)/int(sayi2)
    print("Sonuc:",str(sonuc))


while True:
    pass