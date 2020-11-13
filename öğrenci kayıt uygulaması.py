import sqlite3
bağlanti=sqlite3.connect("database.db")
cursor=bağlanti.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS ögrenciler(okul_no INTEGER,Adi TEXT)""")
def kayit(cursor):
	print("kayıt edilecek öğrencinin")
	ad=str(input("Adı Ve soyadı:"))
	no=int(input("Okul No su:"))
	cursor.execute("""INSERT INTO ögrenciler VALUES({},"{}")""".format(no,ad))
	print("kayıt başarılı")
def öğrenme(cursor):
	bilgi=int(input("bilgi alınacak öğrencinin Okul No sunu girin"))
	cursor.execute("""SELECT * FROM ögrenciler WHERE okul_no={}""".format(bilgi))
	veri=cursor.fetchall()
	for i in veri:
		print("""
		öğrencinin
		adı:{1}
		okul no su:{0}
		""".format(i[0],i[1]))
def sil(cursor):
	bilgi=int(input("silinecek öğrencinin numarası:"))
	cursor.execute("""DELETE FROM ögrenciler WHERE okul_no={}""".format(bilgi))
	print("öğrenci silme başarılı")
while True:
	islem=str(input("öğrenci kayıt için 1\nöğrenci bilgi için 2\nöğrenci silmek için 3\n"))
	if islem=="1":
		kayit(cursor)
	elif islem=="2":
		öğrenme(cursor)
	elif islem=="3":
		sil(cursor)
	bağlanti.commit()
bağlanti.close()
