#cubic spline extra

from sympy import *
x = [1, 2, 3, 4]
y = [1, 5, 11, 8]
X0 = 1.5

h = x[1] - x[0]
n = len(x) - 1
X = symbols('X')
m = symbols('m0:%d' % (n + 1))
M = {0: 0, n: 0}
expr = []

for i in range(1, n):
    expr.append(m[i - 1] + 4 * m[i] + m[i + 1] - 6 * (y[i - 1] - 2 * y[i] + y[i + 1]) / h ** 2)
    for j in M:
        expr[i - 1] = expr[i - 1].subs(m[j], M[j])

sol = solve(tuple(expr), tuple(m))

for i in range(len(sol)):
    M[i + 1] = sol[m[i + 1]]

ind = 0
for ind in range(n + 1):
    if X0 <= x[ind]:
        break

Y = (x[ind] - X0) ** 3 * M[ind - 1] / (6 * h) + (X0 - x[ind - 1]) ** 3 * M[ind] / (6 * h) + (x[ind] - X0) / h * (y[ind - 1] - (h ** 2 * M[ind - 1]) / 6) + (X0 - x[ind - 1]) / h * (y[ind] - h ** 2 * M[ind] / 6)
print(Y)