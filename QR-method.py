from tabulate import tabulate


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


def unity_matrix(n):#produce I_n
    I = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I


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
    A_i = multiplication(H_i, A, N)
    '''print('Ai')
    print_matrix(A_i)'''
    return H_i, A_i


def QR_decomposition(A):#for A n*n
    n = len(A)
    Ai = A
    Q = unity_matrix(n)
    for k in range(n-1):
        Hi, Ai = find_Hi(Ai, k)
        Q = multiplication(Q, Hi, n)
    R = Ai
    return Q, R


def multiplication(A, B, n):#for A and B both n*n
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


def is_upper_tri(A):
    for row in range(len(A)):
        for col in range(row):
            if not A[row][col] == 0:
                return False
    return True


def find_eigenvalues(A):
    x = []
    for i in range(len(A)):
        x.append(A[i][i])
    return x


def QR_method(A, k):
    if k > percision:
        eigen_values = find_eigenvalues(A)
    else:
        Q, R = QR_decomposition(A)
        A_k = multiplication(R, Q, len(A))
        eigen_values = QR_method(A_k, k + 1)
    return eigen_values


def input_matrix(n):
    print("Enter {}*{} matrix in {} lines;Each line contains a row, elements must be separated by space.".format(n, n, n))
    A = []
    for row in range(n):
        r = input().split()
        if not len(r) == n:
            return False
        r = [float(i) for i in r]
        A.append(r)
    return A


percision = 200
n = int(input("Enter n: (number of rows and columns)\n"))
A = input_matrix(n)
#A = [[1, 0, -2], [2, 4, 1], [3, -1, 1]]
#A = [[2, -2, 18], [2, 1, 0], [1, 2, 0]]
#A = [[1, 2, 1], [6, -1, 0], [-1, -2, -1]]
#A = [[1, 2, 3], [2, 3, 5], [0, 1, 1]]
e_vals = QR_method(A, 0)
print("eigenvalues are:")
for i in range(n):
    print(e_vals[i])
