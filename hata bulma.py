from pytube import YouTube
import os
os.system("color b")
while True:
	os.system("cls")
	secim=input("Video İndirmek için 1\nİndirilen Videoları Görüntülemek İçin 2\n")
	if secim=="1":
		url=input("Video Urlsi(ör:https://www.youtube.com/watch?v=34wiI49iBVI):")
		yt = YouTube(url)
		print("Video Bilgileri")
		print("Video Başlığı:",yt.title)
		print("Video Sahibi:",yt.author)
		onay=input("Videoyu İndirmek İstiyormusunuz?(1-evet 2-hayır)")
		if onay=="1":
			print("Video indiriliyor")
			stream = yt.streams.filter(progressive=True).first()
			stream.download()
			print("Video indirildi")
			input("Menüye dönmek için bir tuşa basınız")
		elif onay=="2":
			print("Programdan Çıkılıyor")
			quit()
		else:
			print("Hatalı İşlem")
			input("Menüye dönmek için bir tuşa basınız")
	elif secim=="2":
		print("İndirilen Videolar")
		dizin=os.getcwd()
		dosyalar=os.listdir(dizin)
		dosyalar.remove("youtube video indirici.py")
		a=0
		for i in dosyalar:
			a=a+1
			print("{}.video:{}".format(a,i))
		input("Menüye dönmek için bir tuşa basınız")

