import sys; sys.stdin = open('10830_행렬제곱_G4.txt', 'r')
input = sys.stdin.readline

def double(list):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += list[i][k] * list[k][j]
            tmp[i][j] %= 1000
    return tmp

def multiple(mat1, mat2):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += mat1[i][k] * mat2[k][j]
            tmp[i][j] %= 1000
    return tmp

def power(mat, exp):
    if exp == 0:
        return one
    elif exp == 1:
        return mat

    if exp % 2:
        return multiple(double(power(mat, exp >> 1)), mat)
    else:
        return double(power(mat, exp >> 1))

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
one = [[0] * N for _ in range(N)]
for i in range(N):
    one[i][i] = 1

res = power(matrix, B)
for i in range(N):
    for j in range(N):
        res[i][j] %= 1000
    print(' '.join(map(str, res[i])))




