import sympy as sp


x = sp.Symbol('x')
equation = input("Enter an equation: ")
equation = sp.sympify(equation)
print(repr(equation))


if equation.has(sp.sin) or equation.has(sp.cos) or equation.has(sp.tan):
    angle_mode = input("Enter the angle mode (degrees or radians): ")
    if angle_mode.lower().startswith("d"):
        equation = equation.subs(x, (x*sp.pi / 180))
    elif angle_mode.lower().startswith("r"):
        pass
    else:
        print("Invalid angle mode. Please enter 'degrees' or 'radians'.")
        exit()


try:
    equation = sp.sympify(equation)
    if x not in equation.free_symbols:
        print("The equation must have x in it .")
    else:
        derivatives = int(input("Enter the number of derivatives to calculate: "))
        if derivatives < 0:
            raise ValueError("The number of derivatives must be a non-negative integer.")
        elif derivatives == 0:
            print("The original equation is:", equation)
            exit()
        print("The original equation is:", equation)
        x_values = input("Would you like to evaluate the derivative at a specific x-value? (yes/no): ")

        if x_values.lower().startswith("y"):
            values = float(input("Enter the x-value to evaluate at: "))
        elif x_values.lower().startswith("n"):
            pass
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            exit()

        for i in range(1, derivatives + 1):
            derivative = sp.expand(sp.diff(equation, x, i))
            if i == 1:
                try:
                    critical_points = sp.solve(derivative, x)
                except NotImplementedError:
                    print("Unable to find critical points for the first derivative. ")
                    critical_points = []
            if x_values.lower().startswith("y"):
                derivative_value = derivative.subs(x, values)
                print("Derivatives value = ", derivative_value)

            print("The " + str(i) + " derivative is:")
            print("\n" \
                  "\n" \
                  "f" + "'" * i + "(x)")
            print(sp.pretty(derivative, use_unicode=True))
        print("\n" \
        "" + "=" * 50)
        print((" " * 20) + "CRITICAL POINTS")
        print("=" * 50)
        print("The critical points are:")
        sp.pprint(critical_points, use_unicode=True)

        limit = sp.limit(equation, x, sp.oo)
        neg_limit = sp.limit(equation, x, -sp.oo)

        print("\n" \
        "" + "=" * 50)
        print((" " * 20) + "LIMITS")
        print("=" * 50)

        print("Limit as x approaches positive infinity:")
        sp.pprint(limit, use_unicode=True)

        print("\n" \
        "Limit as x approaches negative infinity:")
        sp.pprint(neg_limit, use_unicode=True)

except (sp.SympifyError, TypeError, ValueError):
    print("Invalid input.")
