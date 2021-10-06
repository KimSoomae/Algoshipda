import sys; read = sys.stdin.readline
from collections import deque

def D(num):
    return (2*num)%10000

def S(num):
    return (num-1)%10000

def L(num):
    ret = num//1000
    red = num%1000
    return red*10 + ret

def R(num):
    ret = num//10
    red = num%10
    return red*1000 + ret

hashmap = {'0':'D','1':'S','2':'L','3':'R'}

def bfs(A,B):
    Q = deque([[A,4]])
    visited = [True]*10000
    visited[A] = False
    while Q:
        num,cmd = Q.popleft()
        for idx, v in enumerate([D(num),S(num),L(num),R(num)]):
            if visited[v]:
                Q.append([v,cmd*10+idx])
                visited[v] = False
                if v == B:
                    return cmd*10+idx

N = int(read().strip())
anw_l = []
for _ in range(N):
    A, B = map(int,read().split())
    anw = list(str(bfs(A,B)))[1:]
    anw_l.append(''.join(hashmap[x] for x in anw))

print('\n'.join(x for x in anw_l))