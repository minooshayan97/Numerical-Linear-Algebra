from tabulate import tabulate


def print_matrix(A):
    print(tabulate(A, tablefmt="plain", numalign="decimal"))


def AX_multiplication(A, X):
    n = len(A)
    AX = []
    for row in range(n):
        m = 0
        for col in range(n):
            m += A[row][col] * X[col]
        AX.append(m)
    return AX


def norm2(x):
    s = 0
    for i in x:
        s += pow(i, 2)
    return pow(s, 0.5)


def vector_plus(x, y):#returns x+y
    n = len(x)
    r = []
    for i in range(n):
        r.append(x[i] + y[i])
    return r


def vector_minus(x, y):#returns x-y
    yy = [-i for i in y]
    return vector_plus(x, yy)


def iteration_matrix_finder(n, method):# create the proper iterative matrix for the given method
    B = []
    C = []
    if method == 'Gauss Seidel':
        for j in range(n):
            C.append(sum([1/pow(4, i+1) for i in range(j+1)]))
        for i in range(n):
            row = [0 for k in range(n)]
            for j in range(1, i+2):
                if j < n:
                    row[j] = 1/pow(4, i-j+2)
            B.append(row)
    elif method == 'Jacobi':
        C = [1/4 for i in range(n)]
        for i in range(n):
            row = [0 for j in range(n)]
            if 0 < i < n-1:
                row[i-1] = 1/4
                row[i+1] = 1/4
            elif i == n-1:
                row[i-1] = 1/4
            else:
                row[i+1] = 1 / 4
            B.append(row)
    return B, C


def iteration(n, method):
    B, C = iteration_matrix_finder(n, method)
    '''
        print('B')
        print_matrix(B)
        print('C')
        print(C)
        '''
    x0 = [1 for i in range(n)]
    x_p = x0
    epsilon = 1
    while epsilon >= percission:
        x_n = vector_plus(AX_multiplication(B, x_p), C)
        epsilon = norm2(vector_minus(x_p, x_n))
        x_p = x_n
    return x_p


def SOR_method(n, w):
    w = float(input('w for SOR\n'))
    x0 = [1 for i in range(n)]
    x_p = x0
    epsilon = 1
    while epsilon >= percission:
        x_n = [0 for i in range(n)]
        x_n[0] = w/4*(1 + x_p[1]) + (1-w) * x_p[0]
        for i in range(1, n-1):
            x_n[i] = w/4 * (1 + x_n[i-1] + x_p[i+1]) + (1-w) * x_p[i]
        x_n[n-1] = w/4*(1 + x_n[n-2]) + (1-w) * x_p[n-1]
        epsilon = norm2(vector_minus(x_p, x_n))
        x_p = x_n
    return x_p


percission = 0.0001
n = int(input())

print('Gauss Seidel result :')
print(iteration(n, 'Gauss Seidel'))

print('Jacobi result :')
print(iteration(n, 'Jacobi'))

print('SOR result :')
print(SOR_method(n, 'SOR'))
