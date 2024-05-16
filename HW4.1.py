
l1 = [0, 1, 0, 12, 3]
l2 = [0]
l3 = [1, 0, 13, 0, 0, 0, 5]
l4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

mass = l1

for i in range(mass.count(0)):
        mass.remove(0)
        mass.append(0)
print(mass)
