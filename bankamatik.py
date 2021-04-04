import os
import time
yoneticiListe = dict()
yoneticiId = 0
bankaListe = dict()
no = 0
def kullaniciParaCek(kullaniciHesapAdi):
	print(f"Merhaba {bankaListe[kullaniciHesapAdi]['ad']}")
	miktar = int(input("Çekeceğiniz TL miktarını giriniz: "))
	if bankaListe[kullaniciHesapAdi]['bakiye'] >= miktar:
		bankaListe[kullaniciHesapAdi]['bakiye'] -= miktar
		print(f"{miktar}TL miktarında paranızı alabilirsiniz!")
	else:
		toplam = bankaListe[kullaniciHesapAdi]['bakiye'] + bankaListe[kullaniciHesapAdi]['ekHesap']
		if toplam >= miktar:
			ekHesapKullanimi = input("Ek Hesap Kullanılsın mı? (e/H): ")
			if ekHesapKullanimi == "e" or ekHesapKullanimi == "E":
				ekHesapKullanilacakMiktar = miktar - bankaListe[kullaniciHesapAdi]['bakiye']
				bankaListe[kullaniciHesapAdi]['bakiye'] = 0
				bankaListe[kullaniciHesapAdi]['ekHesap'] -= ekHesapKullanilacakMiktar
				print(f"{miktar}TL miktarında paranızı alabilirsiniz!")
			else:
				print(f"{bankaListe[kullaniciHesapAdi]['hesapNo']} nolu Hesabınızda {bankaListe[kullaniciHesapAdi]['bakiye']}TL bakiyeniz vardır ve {hesap[kullaniciHesapAdi]['ekHesap']}TL Ek Hesabınızda para bulunmaktadır.")
		else:
			print(f"Bakiyenizde {bankaListe[kullaniciHesapAdi]['bakiye']}TL bulunmaktadır. Bu yüzden işlemi gerçekleştiremezsiniz!")			
	
def kullaniciOlustur():
	global no,bankaListe
	kullaniciHesap = input("Kullanıcı Adı: ")
	if kullaniciHesap in bankaListe:
		print(f"{kullaniciHesap} Adında bir kayıt var.")
		input("İşlemi sonlandırmak için 'Enter' a basınız.")
	if not(kullaniciHesap in bankaListe):
		kullaniciAdi = input("Adınız ve Soyadı: ")
		parola = input("Parola giriniz: ")
		bakiye = int(input("Yatırmak istediği para miktarı: "))
		ekHesap = int(input("Ek hesaba açılan miktar: "))
		no += 1
		kullaniciHesapAdi = kullaniciHesap
		kullaniciHesap = {
		'parola' : parola,
		'ad' : kullaniciAdi,
		'hesapNo' :  no,
		'bakiye' : bakiye,
		'ekHesap' : ekHesap
		}
		bankaListe[kullaniciHesapAdi] = kullaniciHesap
		print("Müşteri başarıyla oluşturuldu!")
		time.sleep(2.5)



def kullaniciParaYatir(kullaniciHesapAdi):
	global bankaListe
	miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
	bankaListe[f"{kullaniciHesapAdi}"]["bakiye"] += miktar
	print("Bakiyeniz: ",bankaListe[f"{kullaniciHesapAdi}"]["bakiye"], "TL' dir.")



def kullaniciEkHesapYukseltme(kullaniciHesapAdi):
	global bankaListe
	miktar = int(input("Ek hesabınızı yükseltmek istediğiniz miktarı giriniz: "))
	bankaListe[f"{kullaniciHesapAdi}"]["ekHesap"] += miktar
	print("Ek Hesabınız: ",bankaListe[f"{kullaniciHesapAdi}"]["ekHesap"], "TL' dir.")



def kullaniciDogrulama(kullaniciHesapAdi,sifre):
	global bankaListe,flag
	if kullaniciHesapAdi in bankaListe:
		if bankaListe[kullaniciHesapAdi]["parola"] == sifre:
			print(f"Sayın {bankaListe[kullaniciHesapAdi]['ad']} başarıyla giriş sağlandı!")
			flag = True
		else:
			if parola == "":
				print("Parola boş bırakılmaz!")
				input("İşlemi sonlandırmak için 'Enter' a basınız.")
				flag = False
			else:
				print("Parolanız yanlıştır.")
				input("İşlemi sonlandırmak için 'Enter' a basınız.")
				flag = False

	else: 
		print(f"{kullaniciHesapAdi} Adında kullanıcı bulunmamaktadır")
		flag = False
	return flag
    


def kullaniciBaskaHesabaParaTransfer(kullaniciHesapAdi):
	global bankaListe
	transferHesapAdi = input("Transfer edilecek hesap kullanıcı adı: ")
	if transferHesapAdi in bankaListe:
		transferMiktar = int(input("Transfer miktarını giriniz: "))
		transferDogrulama = input(f"{transferMiktar}TL tranfer etmek  için işleme devam edilsin mi?(e/H): ")
		if transferDogrulama == "e" or transferDogrulama == "E":
			if bankaListe[kullaniciHesapAdi]['bakiye'] >= transferMiktar:
				print(f"{transferMiktar}TL tranfer edildi!")
				bankaListe[kullaniciHesapAdi]["bakiye"] -= transferMiktar 
				bankaListe[transferHesapAdi]["bakiye"] += transferMiktar
				print(f"{transferMiktar}TL {transferHesapAdi}'na para başarıyla transfer edildi!")
			else:
				toplam = bankaListe[kullaniciHesapAdi]['bakiye'] + bankaListe[kullaniciHesapAdi]['ekHesap']
				if toplam >= transferMiktar:
					ekHesapKullanimi = input("Ek hesap kullanılıp transfer işlemine devam edilsin mi? (e/H): ")
					if ekHesapKullanimi == "e" or ekHesapKullanimi == "E":
						ekHesapKullanilacakMiktar = transferMiktar - bankaListe[kullaniciHesapAdi]['bakiye']
						bankaListe[kullaniciHesapAdi]['bakiye'] = 0
						bankaListe[kullaniciHesapAdi]['ekHesap'] -= ekHesapKullanilacakMiktar
						bankaListe[transferHesapAdi]["bakiye"] += transferMiktar
						print(f"{transferMiktar}TL {transferHesapAdi}'na para başarıyla transfer edildi!")
					else:
						print(f"{bankaListe[kullaniciHesapAdi]['hesapNo']} nolu Hesabınızda {bankaListe[kullaniciHesapAdi]['bakiye']}TL bakiyeniz vardır ve {hesap[kullaniciHesapAdi]['ekHesap']}TL Ek Hesabınızda para bulunmaktadır.")
				else:
					print(f"Bakiyenizde {bankaListe[kullaniciHesapAdi]['bakiye']}TL bulunmaktadır. Bu yüzden işlemi gerçekleştiremezsiniz!")			
			print(f"Hesabınızda {bankaListe[kullaniciHesapAdi]['bakiye']}TL Bakiyeniz Bulunmaktadır!")
			print(f"Ek Hesabınızda {bankaListe[kullaniciHesapAdi]['ekHesap']}TL Bakiyeniz Bulunmaktadır!")		
	else:
		print(f"{transferHesapAdi} Adında kullanıcı yok.")
	os.system("cls")

def kullaniciBilgileri(kullaniciHesapAdi):
	global bankaListe
	if kullaniciHesapAdi in bankaListe:
		print(f"Kullanıcı adınız 	: {kullaniciHesapAdi}")
		print(f"Parolanız 			: {bankaListe[kullaniciHesapAdi]['parola']}")
		print(f"Adınız Soyadınız 	: {bankaListe[kullaniciHesapAdi]['ad']}")
		print(f"Hesap No 			: {bankaListe[kullaniciHesapAdi]['hesapNo']}")
		print(f"Bakiyenizde 		: {bankaListe[kullaniciHesapAdi]['bakiye']}")
		print(f"Ek Hesap Miktarınız : {bankaListe[kullaniciHesapAdi]['ekHesap']}")


def kullaniciBilgiDüzenle(kullaniciHesapAdi,sifre):
	os.system("cls")
	global bankaListe
	if kullaniciHesapAdi in bankaListe:
		while True:
			print(""" 
							[1]   Kullanıcı Adı Güncelleme
							[2]   Ad ve Soyad Güncelleme
							[3]   Parola Güncelleme
							[Q]   Geri
			""")
			kullaniciSecim = input("İşlem Seçiniz: ")
			if kullaniciSecim=="1":
				yeniKullaniciAdi = input("Yeni kullanıcı adınızı giriniz: ")
				if yeniKullaniciAdi in bankaListe:
					print(f"{yeniKullaniciAdi} Adında bir kullanıcı bulunmaktadır!") 
					print("Lütfen başka bir kullanıcı adı giriniz.")
					time.sleep(2.5)
					os.system("cls")
				else:
					yeniListeyeEkleme = bankaListe[kullaniciHesapAdi]
					bankaListe.pop(kullaniciHesapAdi)
					kullaniciHesapAdi = yeniKullaniciAdi
					bankaListe[kullaniciHesapAdi] = yeniListeyeEkleme
					print(f"{kullaniciHesapAdi} Kullanıcı adınız {yeniKullaniciAdi} olarak güncellenmiştir.")
					print("Lütfen Oturumdan Çıkış Yapın ve Tekrar Girin")
					print("Aksi Takdirde İşlemleriniz Geçerli Sayılmayacaktır!")
					input("'Enter' a basın ve oturumundan derhal çıkın!!!")
					os.system("cls")
			if kullaniciSecim == "3":
				if bankaListe[kullaniciHesapAdi]["parola"] == sifre:
					yeniParola = input("Yeni parolanızı giriniz: ")
					bankaListe[kullaniciHesapAdi]["parola"] = yeniParola
					print(f"{sifre} parolanız {bankaListe[kullaniciHesapAdi]['parola']} olarak güncellenmiştir.")
					time.sleep(2.5)
					os.system("cls")
				else:
					print("Girdiğiniz parola hesabınıza ait değil!")
					os.system("cls")
			if kullaniciSecim == "2":
				eskiAdSoyad = bankaListe[kullaniciHesapAdi]["ad"]
				yeniAdSoyad = input("Olmasını istediğiniz Ad Soyad bilgilerini giriniz: ")
				bankaListe[kullaniciHesapAdi]["ad"] = yeniAdSoyad
				print(f"{eskiAdSoyad} Ad Soyad bilgileri {bankaListe[kullaniciHesapAdi]['ad']} şeklinde güncellenmiştir.")
				time.sleep(2.5)
				os.system("cls")
			if kullaniciSecim == "q" or kullaniciSecim == "Q":
				os.system("cls")
				break
			else:
				os.system("cls")
def yoneticiGiris(admin,parola):
	while True:
		global yoneticiListe,yoneticiId
		if admin == "admin" and parola == "1234":
			print( """
						[1]   Yönetici Ekle
						[2]   Müşteri Ekle
						[3]   Yönetici Listele
						[Q]   Yönetici Sayfası Çıkış!
			""")
			yoneticiSecim = input("İşlem Seçiniz: ")


			if yoneticiSecim == "1":
				yoneticiK_Adi = input("Yönetici kullanıcı adı: ")
				yoneticiParola = input("Yönetici parola: ")
				yoneticiId += 1
				yoneticiHesapAdi = yoneticiK_Adi
				yoneticiK_Adi = {
				'YöneticiID' :yoneticiId,
				"YöneticiParola" :	 yoneticiParola 
				}
				yoneticiListe[yoneticiHesapAdi] = yoneticiK_Adi
			elif yoneticiSecim == "2":
				kullaniciOlustur()
				os.system("cls")
			elif yoneticiSecim == "3":
				print(yoneticiListe)
				input("İşlemi sonlandırmak için 'Enter' a basınız.")
				os.system("cls")
			elif yoneticiSecim == "q" or yoneticiSecim == "Q":
				os.system("cls")
				break
			else:
				os.system("cls")
		else:
			print("Hatalı Giriş!")
			input("Çıkmak için 'Enter' a basınız.")
			break
	os.system("cls")

while True:
	os.system("cls")
	while True:
		print(""" 
					[1]   Yönetici Giriş 
					[2]   Müşteri Giriş
					[Q]   Programı Kapat! """)
		panelSecim = input("İşlem Seçiniz: ")
		if panelSecim == "1":
			os.system("cls")
			admin = input("Yönetici Kullanıcı Adı: ")
			parola = input("Yönetici Parola       : ")
			os.system("cls")
			yoneticiGiris(admin,parola)
		elif panelSecim == "2":
			os.system("cls")
			kullaniciHesapAdi = input("Kullanıcı Adınız: ")
			sifre =  input("Parolanız: ")
			os.system("cls")
			kullaniciDogrulama(kullaniciHesapAdi,sifre) 
			while True:
				if flag == True:
					print("""
							[1]   Müsteri Bilgileri
							[2]   Müsteri Bilgileri Güncelle
							[3]   Hesaba Para Yatırma
							[4]   Hesaptan Para Çekme
							[5]   Ek Hesaba Para Yatırma
							[6]   Başka Hesaba Para Transfer Etme
							[Q]	  Hesaptan Çıkış!
							""")
					musteriSecim = input("İşlem Seçiniz: ")
					if musteriSecim=="1":
						os.system("cls")
						kullaniciBilgileri(kullaniciHesapAdi)
						input("İşlemi sonlandırmak için 'Enter' a basınız.")
						os.system("cls")
					elif musteriSecim == "2":
						kullaniciBilgiDüzenle(kullaniciHesapAdi,sifre)
						os.system("cls")
					elif musteriSecim == "3":
						kullaniciParaYatir(kullaniciHesapAdi)
						input("İşlemi sonlandırmak için 'Enter' a basınız.")
						os.system("cls")
					elif musteriSecim == "4":
						kullaniciParaCek(kullaniciHesapAdi)
						input("İşlemi sonlandırmak için 'Enter' a basınız.")
						os.system("cls")
					elif musteriSecim == "5":
						kullaniciEkHesapYukseltme(kullaniciHesapAdi)
						input("İşlemi sonlandırmak için 'Enter' a basınız.")
						os.system("cls")
					elif musteriSecim == "6":
						kullaniciBaskaHesabaParaTransfer(kullaniciHesapAdi)
						input("İşlemi sonlandırmak için 'Enter' a basınız.")
						os.system("cls")
					elif musteriSecim == "q" or musteriSecim == "Q":
						os.system("cls")
						break
					else:
						os.system("cls")
				if flag == False:
					os.system("cls")
					break
		elif panelSecim == "Q" or panelSecim == "q":
			os.system("cls")
			print("İyi Günler...")
			time.sleep(2) 
			os.system("cls")
			quit()
		else:
			os.system("cls")

while True:
    pass

# 1- Programda henüz müşteri olmadığı için müsteri eklemeniz gerek
# 2- Yönetici Giriş- Yönetici Kullanıcı Adı = admin
#					Yönetici Parola = 1234 olarak tanımladım.
#					Giriş yaparak Müşteri Ekleyiniz.
# Not!!!:
#	Eğer Kullanıcı Adı güncelleyecekseniz önce güncelleyiniz daha sonrasında oturumdan
#	çıkmanız gerekmektedir. 
#	Çünkü; kullanıcı adını giriş yaparken tanımladığımız için eski kullanıcı adı aktif olarak görülür 
#	dolayısıyla program hata verir.