import sympy

# inputs and initialization
x = sympy.symbols('x')
expr_text = input("Polynomial P(x) = ")
f = sympy.sympify(expr_text)
df = sympy.diff(f, x)
P = sympy.lambdify(x, f)
dP = sympy.lambdify(x, df)

print(" approximating a zero of this polynomial")

# Newton's method to approximate the result
x_n = float(input("First guess: "))
tolerance = 1e-10
max_iter = 100

for i in range(max_iter):
    x_np1 = x_n - P(x_n) / dP(x_n)
    print(f"x_{i}: {x_np1}")
    print(f"P(x_{i}) = {P(x_np1)}")
    if abs(x_np1 - x_n) < tolerance:
        break
    x_n = x_np1

print(f"Root found: {x_np1:.10f} after {i+1} iterations")
