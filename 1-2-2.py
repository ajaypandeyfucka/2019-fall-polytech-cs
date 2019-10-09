import math
m = int(input("введите количество команд"))
a = (math.factorial(m))
b = (math.factorial(m-3))
f = a/b
print(f"вариантов распределения команд на первые три места {f}")
print(f"вариантов всемозможных распределенийй {a}")
