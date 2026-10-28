total = 0
denom = 1
value = (1/denom)
for i in range(300000):
    total = total + value
    denom = denom + 2
    if i % 2 == 0:
        value = -(1/denom)
    else:
        value = (1/denom)

print(4*total)
