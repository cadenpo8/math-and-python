new = 0
terms = input("How many terms would you like to add? ")
terms = str(terms)
while terms.isdigit() == False:
    terms = int(input("How many terms would you like to add? "))
terms = int(terms)
first = input("First number for your equation: ")
while not first.isnumeric():
    first = input("First number for your equation: ")
first = int(first)
new = int(first)

if terms > 0:
    while terms > 1:
        operator = input("What is your operator? (+, -, /, x, ^) ")
        while operator not in ['+', '-', '/', 'x', '^']:
            operator = input("What is your operator? (+, -, /, x, ^) " )
        first = input("next number for your equation: ")
        while not first.isnumeric():
            first = input("next number for your equation: ")
        new = int(new)
        first = int(first)
        if operator == '+':
            new = first + new
        elif operator == '-':
            new = new - first
        elif operator == '/':
            new = first / new
        elif operator == 'x':
            new = first * new
        elif operator == '^':
            new = (first ** new)
            terms = terms + 1
        terms = terms - 1
print(new)
