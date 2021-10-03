from bisect import bisect_left, bisect_right
import math
cubic = [i**3 for i in range(4000)]
# print(cubic)


def findABC(n):
    for b in range(1, 2000):
        right = n * cubic[b]
        left = right / 2
        left_idx = bisect_left(cubic, left)
        right_idx = bisect_left(cubic, right)
        # print(1,left_idx,right_idx)
        # print(2,left,right)
        # print(3,cubic[left_idx],cubic[right_idx])
        if left_idx > right_idx:
            continue
        for idx in range(left_idx, right_idx):
            k = (right - cubic[idx]) ** (1 / 3)
            if math.isclose(k,round(k)):
                A = idx
                B = b
                C = round((right - cubic[idx]) ** (1 / 3))
                if A+2*B+C < 4000:
                    return A,B,C
                else:
                    return None, None, None
    return None, None, None

while True:
    n = int(input())
    if n == 0:
        break

    if math.isclose(n**(1/3),round(n**(1/3))):
        print('No value.')
        continue

    A,B,C = findABC(n)

    if A:
        print(f'({A}/{B})^3 + ({C}/{B})^3 = {n}')
    else:
        print('No value.')