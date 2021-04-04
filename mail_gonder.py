import smtplib
content="Deneme"
mail=smtplib.SMTP("smtp.gmail.com",587) #hangi sunucuya hangi porttan bağlanacağı
mail.ehlo()#mail yollacağını söylüyoruz
mail.starttls() # verilerimizi encrypt ediyor
mail.login("mailadresiniz","şifreniz") # bağlantımızı sağladık
mail.sendmail("kartal.ahmet1996@gmail.com","kartal.ahmet96@hotmail.com",content)#gönderme işlemi yapıldı
# gmail üzerinden gönderildiği için gmail ayarlarından daha az güvenli uygulamalara izin ver
# seçeneğinin işaretlenmesi gerek.