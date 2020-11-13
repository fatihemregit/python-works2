#for döngüsü ile faktoriyel hesaplama

giris=int(input("Faktoriyeli Hesaplanacak Sayı"))
sayi=1
if giris<=int(-1):
	print("Negatif Sayıların Faktoriyeli Hesaplanamaz")
elif giris>=0:
	
	for i in range(1,giris+1):
		sayi=sayi*i
		
	print("{} sayısının faktoriyeli: {}".format(giris,sayi))
