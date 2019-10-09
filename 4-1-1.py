def determinant(p):
	o = p[::-1]
	if o == p:
		print(p, "- палиндром")
	else:
		print(p, "- не палиндромом")
p = input("Введите число или слово ")
determinant(p)