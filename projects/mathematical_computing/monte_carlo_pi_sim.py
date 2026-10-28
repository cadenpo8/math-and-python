import random

inside = 0
total = 1000000

for i in range(total):
    x = random.random()
    y = random.random()
    
    circle_val = ((x ** 2) + (y ** 2))
    if circle_val <= 1:
        inside = inside + 1

print(4 * (inside / total))
