import sympy as sp

x = sp.Symbol('x', positive=True)
equation = input("Enter an equation: ")
equation = equation.replace("e", "E")
equation = equation.replace("intEgratE", "integrate")
equation = sp.sympify(equation, locals={'x': x})
equation = sp.simplify(equation)
x_value = input("Would you like to evaluate the integral at a specific x-value? (yes/no): ")
if x_value.lower().startswith("y"):
    value_one = float(input("Enter the first x-value to evaluate at: "))
    value_two = float(input("Enter the second x-value to evaluate at: "))
else:
    pass

print(repr(equation))

if equation.has(sp.sin) or equation.has(sp.cos) or equation.has(sp.tan):
    angle_mode = input("Enter the angle mode (degrees or radians): ")
    if angle_mode.lower().startswith("d"):
        equation = equation.subs(x, (x * sp.pi / 180))
    elif angle_mode.lower().startswith("r"):
        pass
    else:
        print("Invalid angle mode. Please enter 'degrees' or 'radians'.")
        exit()

try:
    equation = sp.sympify(equation)
    if x not in equation.free_symbols:
        raise ValueError("The equation must contain the variable 'x'.")
    integrations = input("Enter the number of integrations: ")
    if not integrations.isdigit() or int(integrations) <= 0:
        raise ValueError("The number of integrations must be a positive integer.")
    integrations = int(integrations)
    print("The original equation is:", equation)
    for i in range(integrations):
        integrated_equation = sp.integrate(equation, x, manual=True)
        equation = integrated_equation
        print("The " + str(i + 1) + " integration is: " + str(integrated_equation) + " + C")
        if x_value.lower().startswith("y"):
            integral_value = integrated_equation.subs(x, value_two) - integrated_equation.subs(x, value_one)
            print("The integral value from " + str(value_one) + " to " + str(value_two) + " is: " + str(integral_value))
        if integrated_equation.has(sp.Integral):
            print("No elementary antiderivative was found for the equation (this doesn't mean it doesn't exist or wasnt found).")
            break
        else:
            print("The integrated equation is:")
            sp.pprint(integrated_equation, use_unicode=True)
            print(("+ C" + str(i + 1)))
except (ValueError, TypeError):
    print("Invalid input.")
