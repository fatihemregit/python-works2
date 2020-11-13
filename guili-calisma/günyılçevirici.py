from tkinter import *
pen=Tk()
pen.title("günbulucu")
pen.geometry("300x300")
günlabel01=Label(pen,text=" Kaç Gün:")
günlabel01.place(x=10,y=10)
günentry01=Entry(pen)
günentry01.place(x=70,y=10)#yerleştirme
günlabel02=Label(pen,text="Gün:") #değişmeyecek
günlabel02.place(x=30,y=50)#yerleştirme
günlabel03=Label(pen,text=0)#değişebilir
günlabel03.place(x=60,y=50)#yerleştirme
aylabel01=Label(pen,text="Ay:")#değişmyecek
aylabel01.place(x=30,y=90)#yerleştirme
aylabel02=Label(pen,text=0)#değişebilir
aylabel02.place(x=60,y=90)#yerleştirme
yillabel01=Label(pen,text="Yıl:")#değişmeyecek
yillabel01.place(x=30,y=130)#yerleştirme
yillabel02=Label(pen,text=0)#değişebilir
yillabel02.place(x=60,y=130)#yerleştirme
def g30ba(a0):#gün 30 dan büyükse ay
	ay=int(int(a0)//30)
	return ay
def g30bg(a1):#gün 30 dan büyükse gün
	ay5=int(int(int(a1)//30))
	gün2=int(int(ay5)*30)
	kalangün=int(int(a1)-gün2)
	return kalangün
	
def butonfonksiyon(): #butonun fonksiyonu
	try:
		if int(günentry01.get())<30:
			günlabel03.config(text=günentry01.get())
			aylabel02.config(text=0)
			yillabel02.config(text=0)
		elif int(günentry01.get())>=30:
			ay2=g30ba(günentry01.get())
			gün3=g30bg(günentry01.get())
			günlabel03.config(text=gün3)
			aylabel02.config(text=ay2)
			yillabel02.config(text=0)
			if int(günentry01.get())>=365:
				yil=int(int(günentry01.get())//365)
				yil2=int(yil*365)
				kalangün3=int(int(günentry01.get())-yil2)
				yillabel02.config(text=yil)
				ay4=g30ba(kalangün3)
				gün4=g30bg(kalangün3)
				günlabel03.config(text=gün4)
				aylabel02.config(text=ay4)
	except ValueError:
		print("Lütfen veriyi girin")
buton=Button(pen,text="Dönüştür",command=butonfonksiyon)#buton
buton.place(x=30,y=170)#yerleştirme
kapat=Button(pen,text="Kapat",command=pen.destroy)
kapat.place(x=90,y=170)

pen.mainloop()


