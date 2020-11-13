from tkinter import *
pen=Tk()
veril=Label(pen,text="Ne yazsın?:")
veril.place(x=10,y=20)
verie=Entry(pen)
verie.place(x=75,y=20)
cevap=Label(pen,text="")
def butonfonksiyon():
	cevap.config(text=verie.get())
buton=Button(pen,text=" ekrana bas",command=butonfonksiyon)
kapat=Button(pen,text="Kapat",command=pen.destroy)
buton.place(x=80,y=50)
cevap.place(x=100,y=80)
kapat.place(x=150,y=50)
pen.mainloop()

