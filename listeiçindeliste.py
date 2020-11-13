listem=["a","b","c","d",["e","f",["g","z"],"j",],"aa"]
def listebastir(liste):
	for i in liste:
		if type(i)==type(str()):
			print(i)
		elif type(i)==type(list()):
			listebastir(i)
listebastir(listem)
