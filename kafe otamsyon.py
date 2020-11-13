from os import system as komut
import sqlite3
bağlantı=sqlite3.connect("kafe_otomasyon.db")
cursor=bağlantı.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS hesaplar(masa_no TEXT,hesap BLOB)""")
def hesapekle(connect,cursor):
	print("Hesap Ekleme Menüsü")
	masa=input("masa no:")
	cursor.execute("""SELECT * FROM hesaplar WHERE masa_no='{}'""".format(masa))
	try:
		masaninhesabi=cursor.fetchall()[0][1]
		print("{} nolu masanın hesabı {}".format(masa,masaninhesabi))
		try:
			miktar=float(input("Eklenecek Miktar:"))
			cursor.execute("""SELECT * FROM hesaplar WHERE masa_no='{}'""".format(masa))
			masaninhesabi=cursor.fetchall()[0][1]
			olmasigerekenhesap=masaninhesabi+miktar
			cursor.execute("""UPDATE hesaplar SET hesap={} WHERE masa_no='{}'""".format(olmasigerekenhesap,masa))
			connect.commit()
			print("Başarıyla Hesap eklendi")
		except ValueError:
			print("lütfen sadece noktalı sayı girin")
	except IndexError:
		print("Masa bulunamadı")
	
def hesapsil(connect,cursor):
	print("Hesap Silme Menüsü")
	masa=input("Masa No")
	try:
		cursor.execute("""SELECT * FROM hesaplar WHERE masa_no={}""".format(masa))
		try:
			veri=cursor.fetchall()[0][1]
			print("{} no lu masanın hesabı:{} TL".format(masa,veri))
			try:
				miktar=float(input("Silinecek miktar"))
				if miktar<0:
					print("Miktar negatif sayı olamaz")
				elif miktar>=0:
					anamiktar=veri-miktar
					if anamiktar==float(0.0):
						cursor.execute("""UPDATE hesaplar SET hesap={} WHERE masa_no='{}'""".format(anamiktar,masa))
						connect.commit()
						print("{} no lu masanın hesabı komple silindi".format(masa))
					elif anamiktar !=float(0.0):
						if anamiktar<=float(0.0):
							print("Hesap negatif sayı olamaz")
						elif anamiktar>=float(0.0):
							cursor.execute("""UPDATE hesaplar SET hesap={} WHERE masa_no='{}'""".format(anamiktar,masa))
							connect.commit()
							print("{} no lu masanın şu an ki hesabı {} TL ".format(masa,anamiktar))
			except ValueError:
				print("lütfen sadece noktalı sayı girin")
		except IndexError:
			print("Masa Bulunamadı")
	except sqlite3.OperationalError:
		print("masa bulunamadı")
	
def hesap_görüntüle(connect,cursor):
	print("Masa Görüntüleme Menüsü")
	cursor.execute("""SELECT * FROM hesaplar""")
	veri=cursor.fetchall()
	for i in range(0,10):
		print("{} No lu masanın Hesabı:{}".format(i+1,veri[i][1]))
		
while True:
	komut("cls")
	menü="""Kafe Otomasyon Sistemi
[1] hesap Ekle
[2] Hesap Sil
[3] Hesapları Görüntüle
[q] Çıkış
"""
	secim=input(menü)
	if secim=="1":
		hesapekle(bağlantı,cursor)
		input("Ana menüye dönmek için bir tuşa basın")
	elif secim=="2":
		hesapsil(bağlantı,cursor)
		input("Ana menüye dönmek için bir tuşa basın")
	elif secim=="3":
		hesap_görüntüle(bağlantı,cursor)
		input("Ana menüye dönmek için bir tuşa basın")
	elif secim=="q" or secim=="Q":
		print("Programdan Çıkılıyor...")
		exit()
	else:
		print("Hatalı seçim")
		input("Ana menüye dönmek için bir tuşa basın")
	
