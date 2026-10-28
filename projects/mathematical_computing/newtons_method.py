equation = input("Enter your equation to estimate the answer: ")

equation = equation.replace("-", "+-")
terms = equation.split("+")

derivative_terms = []

for term in terms:
    if "^" in term:
        exponent = int(term.split("^")[1])
    elif "x" in term:
        exponent = 1
    else:
        exponent = 0

    if "x" in term:
        coefficient = int(term.split("x")[0])
    else:
        coefficient = int(term)

    if exponent == 0:
        new_term = "0"
    elif exponent == 1:
        new_term = str(coefficient)
    else:
        new_coefficient = coefficient * exponent
        new_exponent = exponent - 1
        new_term = str(new_coefficient) + "x^" + str(new_exponent)

    derivative_terms.append(new_term)

guess = float(input("What is your estimate: "))

for i in range(20):
    function_value = 0

    for term in terms:
        if "^" in term:
            exponent = int(term.split("^")[1])
        elif "x" in term:
            exponent = 1
        else:
            exponent = 0

        if "x" in term:
            coefficient = int(term.split("x")[0])
        else:
            coefficient = int(term)

        function_value += coefficient * (guess ** exponent)

    derivative_value = 0

    for term in derivative_terms:
        if "^" in term:
            new_exponent = int(term.split("^")[1])
        elif "x" in term:
            new_exponent = 1
        else:
            new_exponent = 0

        if "x" in term:
            new_coefficient = int(term.split("x")[0])
        else:
            new_coefficient = int(term)

        derivative_value += new_coefficient * (guess ** new_exponent)

    estimate = guess - (function_value / derivative_value)
    print("Run: " + str(i) + " Guess: " + str(guess) + " Original function value: " + str(function_value) + " Derivative value: " + str(derivative_value) + " Estimate: " + str(estimate) + "\n"
    "\n"
    "\n")
    guess = estimate

print("Derivative:", derivative_terms)
print("Answer:", round(estimate, 5))
