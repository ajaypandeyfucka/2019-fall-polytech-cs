import time
a = int(input("Число = "))
numbers = {}
lst = []
b = []

start_time = time.time()

def decomposition(n):
	c = 1
	l = 0
	f = 1
	while f <= a:
		f = n ** c
		l = l + a // f
		c += 1
	numbers[n] = l

for n in range(a+1):
	b.append(n)		
i = 2				
while i <= a:		
    if b[i] != 0:	
        lst.append(b[i])
        for j in range(i, a+1, i):
            b[j] = 0
    i += 1

for element in lst:
	n = element
	decomposition(n)
print(numbers)

print("--- %s seconds ---" % (time.time() - start_time))