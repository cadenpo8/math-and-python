total = 0.0
factorial = 1

for n in range(1, 100):
    factorial = factorial * n
    term = 1 / (factorial * n**(1/3))
    total += term

    print("n =", n, "| term =", term, "| total =", total)

print("Final approximation:", total)
