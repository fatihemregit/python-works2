kelime=str(input("Kelimeyi giriniz:"))
yasak=set()
yasakliharfler=("ÇçıİöÖ")
yasaksayi=int(0)
for i in kelime:
	if i in yasakliharfler:
		yasak.add(i)
		
if len(yasak)==0:
	print("kullanılan yasaklı harfler: ")
	print("girilen kelimedeki yasaklı harf sayısı:",0)
elif len(yasak)>=1:
	print("kullanılan yasaklı harfler:",yasak)
	print("girilen kelimedeki yasaklı harf sayısı:",len(yasak))

