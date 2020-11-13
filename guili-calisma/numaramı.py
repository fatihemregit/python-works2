from tkinter import *
pen=Tk()
pen.geometry("500x500")
numarl=Label(pen,text="Gir:")
numarl.pack(pady=10)
numare=Entry(pen)
numare.pack(pady=20)
def numarf():
	try:
		int(numare.get())
		cevap.config(text="Bu Bir Numara.")
	except ValueError:
		cevap.config(text="Bu Bir Numara değil!")
buton=Button(pen,text="tıkla bana",command=numarf)
buton.pack(pady=25)
cevap=Label(pen,text="")
cevap.pack(pady=30)
pen.mainloop()

