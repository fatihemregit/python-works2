from tkinter import *
pen=Tk()
pen.geometry("500x500")
seçinizlabel0=Label(pen,text="Seçiniz:")
seçinizlabel0.place(x=10,y=10)
listboxögeler=["144p","240p","360p","480p","720p","1080p"]

listbox=Listbox(pen,selectmode=EXTENDED)
listbox.place(x=70,y=10)
a=0
for i in listboxögeler:
	a=a+1
	listbox.insert(a,i)
seçiminizlabel=Label(pen,text="Bunu seçtiniz:")
seçiminizlabel.place(x=10,y=200)
seçiminizlabel2=Label(pen,text="Seçim")
seçiminizlabel2.place(x=120,y=200)
def seçimi():
	pass
buton=Button(pen,text="Onayla",command=seçimi)
buton.place(x=10,y=250)
pen.mainloop()
