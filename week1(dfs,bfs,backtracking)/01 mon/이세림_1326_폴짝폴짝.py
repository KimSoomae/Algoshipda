import sys
sys.stdin = open('1326.txt', 'r')

def bfs(a, b, num, N):
    q = []
    q.append(a-1)
    check = [-1]*N
    check[a-1] = 0
    while q:
        node = q.pop(0)
        for n in range(node, N, num[node]):
            if check[n] == -1:
                q.append(n)
                check[n] = check[node] + 1
                if n == b-1:
                    return check[n]
        for n in range(node, -1, -num[node]):
            if check[n] == -1:
                q.append(n)
                check[n] = check[node] + 1
                if n == b-1:
                    return check[n]
    return -1

N = int(input())
num = list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs(a, b, num, N))

