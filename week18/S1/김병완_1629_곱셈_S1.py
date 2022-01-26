import sys; sys.stdin = open('1629_곱셈_S1.txt', 'r')

input = sys.stdin.readline

def power(num, exp, modu):
    if exp == 0:
        return 1
    elif exp == 1:
        return num

    if exp % 2:
        return num * power(num, exp >> 1, modu) ** 2 % modu
    else:
        return power(num, exp >> 1, modu) ** 2 % modu

A, B, C = map(int, input().split())
print(power(A, B, C) % C)
