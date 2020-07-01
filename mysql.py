from collections import Counter
ar=open("n.txt", "r")
lne=0
if ar.mode=="r":
	while True:
		lne+=1
		an=ar.readlines()
		z=len(an)
		if not an:
			break
		for i in range(z):
			z=(an[i].split())
			repeat=Counter(z)
			print(repeat)  

