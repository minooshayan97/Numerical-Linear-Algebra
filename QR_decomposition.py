from tabulate import tabulate


def unity_matrix(n):#produce I_n
    I = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I


def print_matrix(A):
    print(tabulate(A, tablefmt="plain", numalign="decimal"))


def norm2(x):
    s = 0
    for i in x:
        s += pow(i, 2)
    return pow(s, 0.5)


def sgn(x):
    if x > 0:
        return +1
    if x == 0:
        return 0
    return -1


def find_Hi(A, k):
    #print(k)
    N = len(A)
    new_A = [A[i][k:] for i in range(k, N)]
    #print_matrix(new_A)
    n = len(new_A)
    x = [new_A[i][0] for i in range(n)]
    #print(x)
    norm2_x = norm2(x)
    w = [i/norm2_x for i in x]
    v = [-sgn(x[0])] + [0 for i in range(n-1)]
    u = [w[i] - v[i] for i in range(n)]
    norm_u = norm2(u)
    u = [i/norm_u for i in u]
    hi = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1 - 2 * u[i] * u[j])
            else:
                row.append(-2 * u[i] * u[j])
        hi.append(row)
    '''print('hi')
    print_matrix(hi)'''
    H_i =[]
    I = unity_matrix(n)
    for i in range(N-n):
        row = I[i] + [0 for j in range(n)]
        H_i.append(row)
    for i in range(n):
        row = [0 for j in range(N-n)] + hi[i]
        H_i.append(row)
    '''print('Hi')
    print_matrix(H_i)'''
    A_i = AB_multiplication(H_i, A, N)
    '''print('Ai')
    print_matrix(A_i)'''
    return H_i, A_i


def QR_decomposition(A):#for A n*n
    n = len(A)
    Ai = A
    Q = unity_matrix(n)
    for k in range(n-1):
        Hi, Ai = find_Hi(Ai, k)
        Q = AB_multiplication(Q, Hi, n)
    R = Ai
    return Q, R


def AB_multiplication(A, B, n):#for A and B both n*n
    AB = []
    for i in range(n): #row from A
        row = []
        for j in range(n): #col from B
            c_ij = 0
            for k in range(n): #do the summation
                c_ij += A[i][k] * B[k][j]
            row.append(c_ij)
        AB.append(row)
    return AB


def transpose(A):
    n = len(A)
    B = [[0 for col in A] for row in A]
    for row in range(n):
        for col in range(n):
            B[row][col] = A[col][row]
    return B


def AX_multiplication(A, X):
    n = len(A)
    AX = []
    for row in range(n):
        m = 0
        for col in range(n):
            m += A[row][col] * X[col]
        AX.append(m)
    return AX


# solve UX=y
def solve_UX(U, n, Y):
    X = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x_i = (Y[i] - sum([U[i][j]*X[j] for j in range(i+1, n)])) / U[i][i]
        X[i] = x_i
    return X


def solve_by_QR(A, b):
    Q, R = QR_decomposition(A)
    QTb = AX_multiplication(transpose(Q), b)
    x = solve_UX(R, len(A), QTb)
    return x


A = [[2, 3, 1], [5, 1, 2], [2, 8, 1]]
b = [6, 8, 11]
'''
print('Q = ')
print_matrix(Q)
print('R = ')
print_matrix(R)
'''
x = solve_by_QR(A, b)
for i in range(len(A)):
    print('x{} = {}'.format(i, x[i]))
