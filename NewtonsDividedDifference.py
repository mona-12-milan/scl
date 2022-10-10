def proterm(i, value, x):
    pro = 1;
    for j in range(i):
        pro = pro * (value - x[j]);
    return pro;


# Function for calculating
# divided difference table
def dividedDiffTable(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                       (x[j] - x[i + j]));
    return y;


# Function for applying Newton's
# divided difference formula
def applyFormula(value, x, y, n):
    sum = y[0][0];

    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]);

    return sum;


# Function for displaying divided
# difference table
def printDiffTable(y, n):
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t",
                  end=" ");

        print("");


# Driver Code

# number of inputs given
n = 4;
y = [[0 for i in range(10)]
     for j in range(10)];
x = [5, 6, 9, 11];

# y[][] is used for divided difference
# table where y[][0] is used for input
y[0][0] = 12;
y[1][0] = 13;
y[2][0] = 14;
y[3][0] = 16;

# calculating divided difference table
y = dividedDiffTable(x, y, n);

# displaying divided difference table
printDiffTable(y, n);

# value to be interpolated
value = 7;

# printing the value
print("\nValue at", value, "is",
      round(applyFormula(value, x, y, n), 2))


'''
# x = [300, 304, 305, 307]
# y = [2.4771, 2.4829, 2.4843, 2.4871]
# X = 301

x = [2, 2.5, 3]
y = [0.69315, 0.91629, 1.09861]
X = 2.7

n = len(x)
table = []
table.append(y)

for i in range(n - 1):
    values = []
    for j in range(len(table[i]) - 1):
        value = (table[i][j + 1] - table[i][j]) / (x[j + i + 1] - x[j])
        values.append(value)
    table.append(values)

Y = 0

for i in range(len(table)):
    prod = 1
    for j in range(i):
        prod *= (X - x[j])
    Y += prod * table[i][0]

print(Y)
'''
