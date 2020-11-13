
saniye1=int(input("saniye yi giriniz "))
def dakikasaniye(san):
	if san<60:
		print(san,"saniye")
	elif san>=60:
		dak=int(san//60)
		cevir=dak*60
		kalansaniye=san-cevir
		print(dak,"dakika",kalansaniye,"saniye")
def saatim(saniye):
	if saniye<3600:
		dakikasaniye(saniye)
	elif saniye>=3600:
		saat=int(saniye//3600)
		saat2=int(saat*3600)
		kalan_saniye=int(saniye-saat2)
		print(saat,"saat",end=" ")
		dakikasaniye(kalan_saniye)	
saatim(saniye1)
