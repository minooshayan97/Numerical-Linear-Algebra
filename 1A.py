from tabulate import tabulate


def print_matrix(A):
    print(tabulate(A, tablefmt="plain", numalign="decimal"))


def define_tridA(n):
    A = [[0 for j in range(n)] for i in range(n)]
    A[0][0] = A[n - 1][n - 1] = 4
    A[0][1] = A[n - 1][n - 2] = -1
    for i in range(1, n - 1):
        A[i][i] = 4
        A[i][i - 1] = A[i][i + 1] = -1
    return A


def LU_decomposition(A, n):
    A_k = A
    M = [[0 for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = A_k[k][k]
        for row in range(k, n):
            M[row][k] = A_k[row][k] / pivot
        for row in range(k + 1, n):
            for col in range(k + 1, n):
                A_k[row][col] = A_k[row][col] - M[row][k] * A_k[k][col]
        for row in range(k + 1, n):
            col = k
            A_k[row][col] = 0
    return M, A_k


# solve LY=b where b =[1]n
def solve_LY(L, n):
    Y = [0 for i in range(n)]
    for i in range(n):
        y_i = 1 - sum([L[i][j]*Y[j] for j in range(0, i)])
        Y[i] = y_i
    return Y


# solve UX=y
def solve_UX(U, n, Y):
    X = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x_i = (Y[i] - sum([U[i][j]*X[j] for j in range(i+1, n)])) / U[i][i]
        X[i] = x_i
    return X


n = int(input())
A = define_tridA(n)
#A = [[1, 2, 3], [2, 3, 5], [7, 1, 1]]
'''A = [[1, 2, 3, 4, 8],
     [2, 3, 5, 0, 10],
     [7, 1, 1, -9, 5],
     [0.5, 11, 7, 4, -6],
     [3, 18, -14, 1, 4]]
n = len(A)
'''
'''
print("A = ")
print_matrix(A)
'''
L, U = LU_decomposition(A, n)
'''
print("L = ")
print_matrix(L)
print("U = ")
print_matrix(U)
'''
y = solve_LY(L, n)
'''
print("Y = ")
print(y)
'''
x = solve_UX(U, n, y)
print("X = ")
print(x)
