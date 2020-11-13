import sqlite3
bağlanti=sqlite3.connect("kullanicilar.db")
cursor=bağlanti.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS kullanicilar(tür TEXT,kullanci_adi TEXT,parola TEXT)""")
def kullaniciekle(cursor,connect):
	print("Eklenecek Kullanıcının",end="")
	kullanici_adi=input("\nKullanıcı Adı:")
	parola=input("Parola:")
	cursor.execute("""INSERT INTO kullanicilar VALUES('{}','{}','{}')""".format("normal",kullanici_adi,parola))
	connect.commit()
	print("Başarıyla Kullanıcı eklendi.")
def kullanicisil(cursor,connect,kullanici_adi):
	cursor.execute("""DELETE FROM kullanicilar WHERE kullanci_adi='{}'""".format(kullanici_adi))
	connect.commit()
	print("Başarıyla kullanıcı silindi.")
dkullanicilar=list()
cursor.execute("""SELECT * FROM kullanicilar""")
veri=cursor.fetchall()
for i in veri:
	dkullanicilar.append(i[1])
while True:
	kullanici_adi=input("Kullanıcı Adı:")
	if kullanici_adi in dkullanicilar:
		parola=input("Parola:")
		cursor.execute("""SELECT * FROM kullanicilar WHERE kullanci_adi='{}'""".format(kullanici_adi))
		veri2=cursor.fetchall()
		dparola=veri2[0][2]
		if parola==dparola:
			break
		elif parola!=dparola:
			print("parola yanlış")
	elif kullanici_adi not in dkullanicilar:
		print("{} adlı kullanıcı bulunamadı".format(kullanici_adi))
def sifredegistir(cursor,connect,kulllanici):
	yeniparola=input("Lütfen {} Kullanıcısının Yeni Parolasını Girin".format(kulllanici))
	cursor.execute(""" UPDATE kullanicilar SET parola ='{}' WHERE kullanci_adi='{}'""".format(yeniparola,kulllanici))
	connect.commit()
	print("Başarıyla {} Kullanıcısının parolası değiştirildi Yeni parolası: {}".format(kulllanici,yeniparola))



while True:
	cursor.execute("""SELECT * FROM kullanicilar WHERE kullanci_adi='{}'""".format(kullanici_adi))
	try:
		tür=cursor.fetchall()[0][0]
	except IndexError:
		print()
	if tür=="ana":
		print(" Kullanıcı Yönetim menüsü")
		menu="[1] Kendi şifremi Değiştir\n[2]Başka Kullanıcı Ekleme\n[3]Başka Kullanıcı Silme\n[q]Çıkış\n"
		islem=input(menu)
		if islem=="1":
			sifredegistir(cursor,bağlanti,kullanici_adi)
		elif islem=="2":
			kullaniciekle(cursor,bağlanti)
		elif islem=="3":
			baskakullanici=input("Silincek kullanıcının\n Kullanıcı Adı:")
			kullanicisil(cursor,bağlanti,baskakullanici)
		elif islem=="q" or islem=="Q":
			print("Programdan Çıkılıyor...")
			quit()
		else:
			print("listede olmayan bir işlem seçtiniz")
	elif tür!="ana":
		print("Hoşgeldiniz lütfen işleminizi seçin")
		islem2=input("[1]Kendi Şifremi Değiştirme\n[2]Kendi kullanıcımı Silme\n[q]Çıkış\n")
		if islem2=="1":
			sifredegistir(cursor,bağlanti,kullanici_adi)
		elif islem2=="2":
			kullanicisil(cursor,bağlanti,kullanici_adi)
		elif islem2=="q" or islem2=="Q":
			print("Programdan Çıkılıyor...")
			quit()
		else:
			print("liste dışı bir işlem seçtiniz")
		
