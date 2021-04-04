import platform
import time
import os
import signal
import datetime

from datetime import time

try:
    from Tkinter import *
    from Tkinter import ttk
    import tkMessageBox
except ImportError:
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox

entry_width = 2
root = Tk()
root.title("KAPATMA AYARI")
root.geometry("280x165+720+250")
root.resizable(width=False, height=False)

top_label_font = ("verdana",12)
time_font = ("verdana",26)
def hakkında():
    yeniPencere=Toplevel()
    baslik2=yeniPencere.title("Program Hakkında")
    yazı=Label(yeniPencere,text="Edit:AGOLA\nÇıkış Tarihi:10.10.2020",fg="white",font="Times 22 bold",cursor="circle",bg="black")
    yazı.pack()
    yeniPencere.geometry("290x70+700+500")
    yeniPencere.resizable(width=FALSE,height=FALSE)



menu=Menu(root)
root.config(menu=menu)
menuDosya2=Menu(menu,tearoff=0)
menu.add_cascade(label="Hakkında",command=hakkında)



def shutdown():
	root.geometry("240x120+720+250")
	root.title("KAPANIYOR")
	label1.grid_forget()
	label2.grid_forget()
	label3.grid_forget()
	time_frame.grid_forget()
	hours.grid_forget()
	minutes.grid_forget()
	seconds.grid_forget()
	shutdown_button.grid_forget()
	sayim_label.grid(row=0, column=0, pady=0, padx=10)
	abort_button.grid(row=0, column=0, pady=10, padx=10)
	hour = hours.get()
	checkN(hour)
	minute = minutes.get()
	checkN(minute)
	second = seconds.get()
	checkN(second)
	times = to_seconds(hour, minute, second)

	if platform.system() == 'Windows':
		command = "shutdown /s /t " + str(times)

	elif platform.system() == 'Linux':
		command = 'sudo shutdown -P +' + to_minutes(times)

	print(command)
	os.system(command)
	tarih=datetime.datetime.now()
	saat=tarih.hour
	dakika=tarih.minute
	saniye=tarih.second
	toplam=to_seconds(saat,dakika,saniye)
	zaman=toplam+times
	bitis = str(datetime.timedelta(seconds=zaman))
	sayim_label.config(text="Kapanma Saati:\n"+bitis)
	messagebox.showwarning('Uyarı', 'İptal etmeden prgoramdan çıkarsan, bilgisayarın belirli sürede kapanacaktır.',icon='warning')

def abort():
    sayim_label.config(text="İptal Edildi")
    if platform.system() == 'Windows':
        command = 'shutdown /a'
    elif platform.system() == 'Linux':
        command = 'sudo shutdown -c'
    else:
        command = 'echo "os not compatible"'
    print(command)
    os.system(command)


def to_seconds(h,m,s):
    return int(h)*3600+int(m)*60+int(s)


def to_minutes(time):
	return str(time//60)



def checkN(n):
	try:
		n = int(n)
	except ValueError:
		try:
			messagebox.showerror("Error", "Sadece sayı girinizi")
		except:
			ttk.MessageBox.showerror("Error", "Sadece sayı giriniz")
		sys.exit(0)



label1 = ttk.Label(root,text='Ne kadar süre içinde kapatılsın', font=top_label_font)
label1.grid(row=0,column=0,pady=10,padx=10)

time_frame = ttk.Frame(root)
time_frame.grid(row=2,column=0,padx=10,pady=10)

hours = ttk.Entry(time_frame, font=time_font,width=entry_width) #
hours.insert(0, '00')
hours.grid(row=0,column=1)

label2 = ttk.Label(time_frame,text=':', font=time_font)
label2.grid(row=0,column=2)

minutes = ttk.Entry(time_frame, font=time_font,width=entry_width) #
minutes.insert(0, '00')
minutes.grid(row=0,column=3)

label3 = ttk.Label(time_frame,text=':', font=time_font)
label3.grid(row=0,column=4)

seconds = ttk.Entry(time_frame, font=time_font,width=entry_width) #
seconds.insert(0, '00')
seconds.grid(row=0,column=5)

button_frame = ttk.Frame(root)
button_frame.grid(row=3,column=0)

shutdown_button = ttk.Button(button_frame, text="AYARLA",cursor="exchange",command=lambda:shutdown())   # shutdown Button
shutdown_button.grid(row=0,column=1,pady=10,padx=10)

abort_button = ttk.Button(button_frame, text='İPTAL ET',command=lambda:abort())        # abort button
abort_button.forget()

sayim_label= Label(root,font=("verdana",20), foreground= "red")
sayim_label.forget()

root.mainloop()