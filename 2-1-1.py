import random
import time
idd = []
dub = []
k = 10000

def iteration(idd):
	for j in range(k-1):
		if idd[j] == idd[j+1]:
			dub.append(idd[j])
		else: pass

for i in range(k):
	m = random.randint(3000, 7000)
	idd.append(m)
idd.sort()


start_time = time.time ()
iteration(idd)
print("Время поиска равно %s секунд" % (time.time() - start_time))


dub.insert(0, "Есть дубликаты : ")
print(dub)

