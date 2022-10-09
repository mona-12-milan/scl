import sympy as sp


def find_sides(x_values, x):
    lower = x_values[0]
    higher = x_values[len(x_values) - 1]
    high_count = 0
    low_count = 0
    for i in x_values:
        if i - x > lower - x and i - x < 0:
            lower = i
        if i - x < higher - x and i - x > 0:
            higher = i
    return [lower, higher, x_values.index(lower), x_values.index(higher)]


def constant_eval(x_values, y_values):
    n = len(x_values)
    Ms = []
    for i in range(n):
        Ms.append(sp.symbols('m' + str(i)))
    equations = []
    for i in range(1, n - 1):
        h = x_values[i] - x_values[i - 1]
        equation = Ms[i - 1] + 4 * Ms[i] + Ms[i + 1] - (6 / h ** 2) * (
                    y_values[i - 1] - 2 * y_values[i] + y_values[i + 1])
        equation = equation.evalf(subs={Ms[0]: 0, Ms[n - 1]: 0})
        equations.append(equation)
    constant = sp.solve(equations)
    Ms = [0]
    for i in constant:
        Ms.append(constant[i])

    Ms.append(0)
    print(Ms)
    return Ms


def cubicbSpline(xi, x, xii, mi, mii, yi, yii):
    y = (1 / 6) * mi * (xii - x) ** 3 + (1 / 6) * mii * (x - xi) ** 3 + (xii - x) * (yi - (1 / 6) * mi) + (x - xi) * (
                yii - (1 / 6) * mii)
    return y


x_values = [0, 1, 2, 3]
y_values = [1, 2, 9, 28]
x = 2.5
sides = find_sides(x_values, 2.5)
constants = constant_eval(x_values, y_values)
print(cubicbSpline(sides[0], x, sides[1], constants[sides[2]], constants[sides[3]], y_values[sides[2]],
                   y_values[sides[3]]))