H = input("Сколько людей в стране? ")
P = int(H)
allp = 0							
boys = 0								
F = 0
if (int(H) % 2) == 0:                           
    print(H)
else:
    H=int(H) - 1
while int(H) > 0:
    import random
    r = random.randint(0, 1)
    if r == 0:
        F = F + 1
        allp = allp + 1

        print("Родилось " + str(allp) + " детей, из них мальчиков: " + str(boys))
    else:
        boys = boys + 1
        H = int(H) - 2
        allp = allp + 1
        print("Родилось " + str(allp) + " детей, из них мальчиков: " + str(boys))
P = P + allp
if (P % 2) == 0:
    PP = P / 2
else:
    PP = (P - 1) / 2
print("Количество людей после = " + str(P))
k = (F + PP) / (boys + PP)
women = F + PP
men = boys + PP
print("Отношение количества женщин(" + str(women) +") к количеству мужчин (" + str(men) +") равно " + str(k))