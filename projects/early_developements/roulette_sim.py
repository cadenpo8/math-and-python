import random

money = 1000
keep_going = True

print("Welcome to Roulette")
print("You start with $1000")

while keep_going == True:

    print("Current balance:", money)

    while True:
        try:
            bet = float(input("How much would you like to bet: "))
            if bet > money:
                print("You cannot bet more than your balance:", money)
            elif bet <= 0:
                print("Enter a positive number")
            else:
                break
        except ValueError:
            print("Invalid response, please enter a number")

    money = money - bet

    type_bet = input("What would you like to bet on (number, color, even, odd): ").lower()

    while type_bet not in ["number", "color", "even", "odd"]:
        type_bet = input("Please choose number, color, even, or odd: ").lower()

    number = random.randint(0, 36)

    if type_bet == "even":
        print("Roulette landed on", number)
        if number != 0 and number % 2 == 0:
            print("You won")
            money = money + (bet * 2)
        else:
            print("You lost")

    elif type_bet == "odd":
        print("Roulette landed on", number)
        if number % 2 != 0:
            print("You won")
            money = money + (bet * 2)
        else:
            print("You lost")

    elif type_bet == "color":
        color = input("Choose red or green: ").lower()

        if color.startswith("r"):
            chosen_color = "red"
        else:
            chosen_color = "green"

        wheel_color = random.choice(["red", "green"])

        print("The wheel landed on", wheel_color)

        if chosen_color == wheel_color:
            print("You won")
            money = money + (bet * 2)
        else:
            print("You lost")

    else:
        try:
            chosen_number = int(input("What number would you like to bet on (0-36): "))
        except ValueError:
            chosen_number = -1

        print("Roulette landed on", number)

        if chosen_number == number:
            print("You won big")
            money = money + (bet * 35)
        else:
            print("You lost")

    if money <= 0:
        print("You are out of money")
        break

    again = input("Keep playing? (y/n): ").lower()

    if again != "y":
        keep_going = False

print("You finished with", money)
