					
uron = int(input("Ввод числа "))
first = 1140671485				
second = 128201163
final = (2**32) // 1000000
def rand(lcg):
	uron = ((uron * first + second) % final)
	print ("Урон будет равен =" + uron)
	return(uron)
for i in range(2):
	rand(uron)