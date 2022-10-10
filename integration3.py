from sympy import *
x = symbols('x')

#trapezodial_2

X = [1.4	, 1.6	, 1.8	, 2.0	, 2.2	]
Y = [4.0552, 4.9530, 6.0436, 7.3891, 9.0250]

h = X[1] - X[0]

value = (h / 2) * (Y[0] + 2 * sum(Y[1:-1]) + Y[-1])

print((value))


#simpsons_13_2

eq = log(x)
limits = [4, 5.2]

h = 0.1
X = []
Y = []
ind = limits[0]

while ind <= limits[1]:
    X.append(ind)
    Y.append(eq.subs(x, ind))
    ind += h

value = (h / 3) * (Y[0] + 4 * sum(Y[1:-1:2]) + 2 * sum(Y[2:-1:2]) + Y[-1])

print(N(value))

#simpsons_38_2
eq = log(x)
limits = [4, 5.2]

h = 0.1
X = []
Y = []
ind = limits[0]

while ind <= limits[1]:
    X.append(ind)
    Y.append(eq.subs(x, ind))
    ind += h

total = 0
total3 = 0
for i in range(1, len(Y) - 1):
    if i % 3 != 0:
        total += Y[i]
    else:
        total3 += Y[i]


value = (3 * h / 8) * (Y[0] + 2 * total3 + 3 * total + Y[-1])

print((value))