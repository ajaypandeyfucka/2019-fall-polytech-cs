c = 0
a, b = [ int(i) for i in input("введите 2 числа ").split() ]
if (a == 0) or (b == 0):
    c = 0
elif a > 0 and b > 0:
	for i in range(b):
		c = c + a
elif a < 0 and b < 0:
	a = - a
	b = - b
	for i in range(b):
		c = c + a
elif a > 0 and b < 0:
	b = b - b - b
	for i in range(b):
		c = c + a
	c = -c
else:
	a = a - a - a
	for i in range(b):
		c = c + a
	c = -c
print(a, "*", b, "=", c)
