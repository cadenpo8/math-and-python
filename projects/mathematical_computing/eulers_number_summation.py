e = 0
total = 1
runs = 10000

for i in range(runs):
    if i > 0:
        total *= i
    e += 1 / total

print(e)
