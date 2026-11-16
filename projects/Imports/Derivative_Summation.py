import sympy as sp
deriv_val = 0
equation = input("Enter the equation: ")
x = sp.symbols('x')
equation = sp.sympify(equation)
value = float(input("Enter the value of x: "))

if equation.has(sp.sin(x)) or equation.has(sp.cos(x)) or equation.has(sp.tan(x)):
    radian = input("Is the angle in radians? (yes/no): ")
    if radian.lower().startswith('y'):
        value = sp.rad(value)
    else:
        value = sp.deg(value)

for i in range(1, 6):
    derivative = sp.diff(equation, x, i)
    derivative_value = derivative.evalf(subs={x: value})
    deriv_val += derivative_value

print("The sum of the first 5 derivatives evaluated when x =", value, "is:", deriv_val)
