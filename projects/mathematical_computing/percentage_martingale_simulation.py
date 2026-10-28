import random
money = 2000
percent_bet = 1
spin = 0
highest_money = money
while money > 0:
    spin = spin + 1
    bet = (percent_bet/100) * money
    winning_num = random.randint(1, 38)
    if winning_num <= 18:
        money = money + bet
        percent_bet = 2.5
    else:
        percent_bet = percent_bet * 2
        money = money - bet
    if money > highest_money:
        highest_money = money
    print(str(spin) + "\n"
    "Your total is: $" + str(money))

print("Your highest amounts was: $" + str(highest_money))
