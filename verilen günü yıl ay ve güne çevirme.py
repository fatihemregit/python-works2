gün=int(input("gün sayısını giriniz: "))
def günhesapla(günsayisi):
	if günsayisi<30:
		print("0 ay",günsayisi,"gün")
	else:
		ay=int(günsayisi//30)
		cevir=int(ay*30)
		kalangün=günsayisi-cevir
		print(ay,"Ay",kalangün,"Gün")
	
def yilhesapla(günsayi):
	if günsayi<365:
		günhesapla(günsayi)
	else:
		yil=int(günsayi//365)
		cevir2=int(yil*365)
		kalan2gün=int(günsayi-cevir2)
		print(yil,"Yıl",end=" ")
		günhesapla(kalan2gün)
yilhesapla(gün)
