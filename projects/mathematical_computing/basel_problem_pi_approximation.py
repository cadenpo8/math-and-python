total = 0
for i in range(10000000):
    total = total + (1 / ((i+1) ** 2))
total = total * 6
total = total ** 0.5
print(total)
