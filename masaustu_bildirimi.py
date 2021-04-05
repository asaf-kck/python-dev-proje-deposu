# pip install win10toast diyerek bu kütüphanemizi import ediyoruz.
from win10toast import ToastNotifier

bildirim = ToastNotifier()
# win10toast kütüphanemizin altında bulunan ToastNotifier classını çağırıyoruz

bildirim.show_toast(title='Windows Güvenlik Duvarı', msg='Bilgisayarınız ciddi bir virüs ile karşılaştı', icon_path=None, duration=5)
# bildirim.show_toast() dedikten sonra, bir mesaj başlığı "title='' ", bir mesaj içeriği "msg='' ", bir mesaj iconu belirtmek için "icon_path='' ", bildirimin ekranda kaç saniye kalacağını belirtmek için "duration= "