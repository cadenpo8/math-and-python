print("Josephus Problem Simulator\n"
"\n")

amt_people = int(input("How many people would you like to be in the circle?: "))
start = int(input("At which person would you like to start at?: "))
skip_people = int(input("How many people down would you like to kill?: "))

if skip_people < 2:
    winner = int(amt_people)
    print("Your winner is: " + str(winner) + "!")

else:
    people = list(range(1, amt_people + 1))
    position = start - 1

    while len(people) > 1:
        position = (position + skip_people - 1) % len(people)
        people.pop(position)

        if position == len(people):
            position = 0

    winner = people[0]
    print("Your winner is: " + str(winner) + "!")
