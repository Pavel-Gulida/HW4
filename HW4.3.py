import random

mass = []
for i in range(random.randint(3,10)):
    mass.append(random.randint(1,100))

mass1 = []
mass1.append(mass[0])
mass1.append(mass[2])
mass1.append(mass[-2])

print(mass)
print(mass1)
