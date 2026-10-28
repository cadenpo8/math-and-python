import random

number_choice = int(input("What number would you like to simulate until single: "))

total_final = 0

for i in range(1000):

    num = random.randint(0, number_choice)
    total = 0
    value = num

    while True:
        total = total + (value % 10)
        value = value // 10

        if value == 0:
            while total >= 10:
                value = total
                total = 0

                while value > 0:
                    total = total + (value % 10)
                    value = value // 10

            break

    total_final = total

print("Your choice: " + str(number_choice) + "\n"
"Your total digit value: " + str(total))
