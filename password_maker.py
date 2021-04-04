import random
import time
dosya = open("Şifre.txt","a") 


işkem = ["q", "w", "e", "r", "t", "y", "u", "ı", "o", "p", "ğ", "ü", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ş", "i", "z", "x", "c", "v", "b", "n", "m", "ö", "ç", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Ğ", "Ü", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ş", "İ", "Z", "X", "C", "V", "B", "N", "M", "Ö", "Ç", "!", "^", "+", "%", "&", "/", "(", ")", "=", "?", "_", "-"]
#Şifremizde olabilcek karakterleri girdik#

print("---Otomatik Şifre yapıcı---")
time.sleep(3)
print("\n \n \n \n \n")
print("Lütfen Şİfre uzunluğu girin")
print("min. 8, max. 20 olabilir")
uzun = input(">>>")
#Şİfre uzunluğumuzu giriyoruz#


i = 0
#-------------------------------#
if uzun == "8" :
    for i in range(8):
        index = random.choice(işkem)  
        dosya.write(str(işkem))
#-------------------------------#
if uzun == "9" :
    for i in range(9):
        index = random.choice(işkem)
        dosya.write(str(index)) 
#-------------------------------#
if uzun == "10":
    for i in range(10):
        index = random.choice(işkem)
        dosya.write(str(index)) 
#-------------------------------#
if uzun == "11":
    for i in range(11):
        index = random.choice(işkem)
        dosya.write(str(index))
#-------------------------------#
if uzun == "12":
    for i in range(12):
        index = random.choice(işkem)
        dosya.write(str(index))
#-------------------------------#
if uzun == "13":
    for i in range(13):
        index = random.choice(işkem)
        dosya.write(str(index))
#-------------------------------#
if uzun == "14":
    for i in range(14):
        index = random.choice(işkem)
        dosya.write(str(index))
#-------------------------------#
if uzun == "15":
    for i in range(15):
        index = random.choice(işkem)
        dosya.write(str(index))
#-------------------------------#
if uzun == "16":
    for i in range(16):
        index = random.choice(işkem)
        dosya.write(str(index))
#-------------------------------#
if uzun == "17":
    for i in range(17):
        index = random.choice(işkem)
        dosya.write(str(index))
#-------------------------------#
if uzun == "18":
    for i in range(18):
        index = random.choice(işkem)
        dosya.write(str(index))
#-------------------------------#
if uzun == "19":
    for i in range(19):
        index = random.choice(işkem)
        dosya.write(str(index))
#-------------------------------#
if uzun == "20":
    for i in range(20):
        index = random.choice(işkem)
        dosya.write(str(index))

if float(uzun) > 20 or float(uzun) <0:
    print("Bu uzunlukta şifre yapmak akla zarar. Tekrar başlat.")
    exit()

print("Şifre hazırlanıyor")
dosya.write("----------------------------------")
dosya.close()
for ı in range(100):
    print("%", ı)
    time.sleep(0.05)
print("Bitti")
time.sleep(2)
print("Şifreniz", dosya.name, "Dan alabilirsiniz")
time.sleep(3)
print("Lütfen şifrenizi aldıktan sonra siliniz")