summa = int(input("Сумма равна "))
def Conversion():
	 Ch= summa
	date = []
	while Ch > 0:
		number = Ch % 10
		if number == 1:
			date.append ("один")
		elif number == 2:
			date.append ("два")
		elif number == 3:
			date.append ("три")
		elif number == 4:
			date.append ("четыре")
		elif number == 5:
			date.append ("пять")
		elif number == 6:
			date.append ("шесть")
		elif number == 7:
			date.append ("семь")
		elif number == 8:
			date.append ("восемь")
		elif number == 9:
			date.append ("девять")
		else:
			date.append ("ноль")
		Ch //= 10
	date.reverse() 
	date.insert(0, summa)
	date.insert(1, ":")
	print(*date, sep = ' ')
Conversion()