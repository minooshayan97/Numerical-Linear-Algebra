def define_tridA(n):
    A = [[0 for j in range(n)] for i in range(n)]
    A[0][0] = A[n - 1][n - 1] = 4
    A[0][1] = A[n - 1][n - 2] = -1
    for i in range(1, n - 1):
        A[i][i] = 4
        A[i][i - 1] = A[i][i + 1] = -1
    return A


def gaussian_elimination(A, n):
    m = [0 for i in range(n)]
    b = [0 for i in range(n)]
    m[0] = 4
    b[0] = 1
    for row in range(1, n):
        co = 1 / m[row-1]
        b[row] = 1 + co * b[row-1]
        m[row] = 4 - co
    x = [0 for i in range(n)]
    x[n-1] = b[n-1] / m[n-1]
    for row in range(n-2, -1, -1):
        x[row] = (b[row] + x[row + 1]) / m[row]
    return x


n = int(input())
A = define_tridA(n)
x = gaussian_elimination(A, n)
print("X = ")
print(x)
