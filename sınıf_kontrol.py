# Sınıflardaki öğrencilerin listesi
a_sinifi=["ahmet","mehmet"]
b_sinifi=["ayşe","fatma"]
# Denetliyeceğimiz isimi girmemiz içindir
isim=input("İsim Giriniz:")

# Eğer a sınıfındaysa yazacağı şey
if isim in a_sinifi:
    print("Kişi (A) sınıfındadır.")

# Eğer b sınıfındaysa yazacağı şey
elif isim in b_sinifi:
    print("Kişi (B) sınıfındadır.")

# Öyle biri yoksa vereceği cevap
else:
    print("Sistem böyle bir kişiyi bulamadı")


while True:
    pass