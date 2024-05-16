
l1 = [1, 3, 5]
l2 = [6]
l3 = []

mass = l2

sum = 0
for i in range(len(mass)):
    if i % 2 == 0:
        sum += mass[i] * mass[-1]
print(sum)