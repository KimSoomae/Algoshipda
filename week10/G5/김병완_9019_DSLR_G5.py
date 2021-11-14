import sys; sys.stdin = open('9019_DSLR_G5.txt', 'r')
from collections import deque
input = sys.stdin.readline


def S(num):
    if num == 0:
        return 9999
    else:
        return num - 1

def L(num):
    T = num // 1000
    H = (num % 1000) // 100
    D = (num % 100) // 10
    O = (num % 10)

    return H * 1000 + D * 100 + O * 10 + T

def R(num):
    T = num // 1000
    H = (num % 1000) // 100
    D = (num % 100) // 10
    O = (num % 10)

    return O * 1000 + T * 100 + H * 10 + D

def bfs(start, target):
    Q = deque()
    dp[start] = ['Start']
    Q.append(start)
    while Q:
        num = Q.popleft()
        tmp = [(num * 2) % 10000, num - 1 if num != 0 else 9999, L(num), R(num)]
        # if num == target:
        #     result = tup
        #     break
        for i in range(4):
            if dp[tmp[i]]: continue
            dp[tmp[i]] = [letter[i], num]
            Q.append(tmp[i])
            if dp[target]:
                return
            # if i == 0:
            #     tmpNum = D(num)
            #     tmp = tup
            #     tmp += ('D',)
            #     Q.append((tmpNum, tmp))
            # elif i == 1:
            #     tmpNum = S(num)
            #     tmp = tup
            #     tmp += ('S',)
            #     Q.append((tmpNum, tmp))
            # elif i == 2:
            #     tmpNum = L(num)
            #     tmp = tup
            #     tmp += ('L',)
            #     Q.append((tmpNum, tmp))
            # elif i == 3:
            #     tmpNum = R(num)
            #     tmp = tup
            #     tmp += ('R',)
            #     Q.append((tmpNum, tmp))
    # return result

for tc in range(int(input())):
    A, B = map(int, input().split())
    letter = ['D', 'S', 'L', 'R']
    dp = [[] for _ in range(10001)]
    if A == B:
        print('')
        continue
    bfs(A, B)
    result = []
    while True:
        result.append(dp[B][0])
        if dp[B][1] == A:
            break
        B = dp[B][1]
    print(*result[::-1], sep='')
    # print(''.join(bfs(A, B)[1:]))
    # print(L(5), L(0))
    # print(R(123))
