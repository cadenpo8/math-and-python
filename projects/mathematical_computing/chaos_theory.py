r = 3.56969
x = .5
values = []

for i in range(10000):
    x = r * x * (1 - x)
    values.append(x)
    
print("Last 64 values: ")
for value in values[-512:]:
    print(round(value, 10))
for period in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
    if abs(values[-1] - values[-1-period]) < 1e-10:
        print("Possible cycle:", period)
