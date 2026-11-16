import sympy as sp

variable = sp.symbols('x')
integral = sp.integrate(sp.sqrt(variable), (variable, 0, 100))
integral = integral.simplify()
integral = integral.evalf()
total = 0
terms = []
for i in range(100):
    terms.append(i)
for terms in terms:
    sqrt_term = sp.sqrt(terms)
    sqrt_term = sqrt_term.simplify()
    sp.pprint(sqrt_term)
    total = total + sqrt_term
total = total.evalf()

print(" \n" \
"\n" \
)
print("Your total summation is: ")
sp.pprint(total)
print("\n" \
"\n" \
)
print("Your integral is: ")
sp.pprint(integral)

print("\n" \
"\n" \
)
print("The difference between the integral and the summation is: ")
sp.pprint(integral - total)
