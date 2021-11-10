input = open('input.txt').readline
from collections import deque

def NS(x):
    if x == '1':
        return 'S'
    return 'N'

def my_rotate(N, d):
    sample = [T1[2], T2[6], T2[2], T3[6], T3[2], T4[6]]

    if N == 0:
        T1.rotate(d)
        if sample[0] != sample[1]:        
            T2.rotate(-d)
            if sample[2] != sample[3]:
                T3.rotate(d)
                if sample[4] != sample[5]:
                    T4.rotate(-d)    
    elif N == 1:
        T2.rotate(d)
        if sample[0] != sample[1]:
            T1.rotate(-d)
        
        if sample[3] != sample[2]:
            T3.rotate(-d)
            if sample[4] != sample[5]:
                T4.rotate(d)
        return
    
    elif N == 2:
        T3.rotate(d)
        if sample[4] != sample[5]:
            T4.rotate(-d)
        
        if sample[2] != sample[3]:
            T2.rotate(-d)
            if sample[0] != sample[1]:
                T1.rotate(d)
        
    else:
        T4.rotate(d)
        if sample[4] != sample[5]:
            T3.rotate(-d)
            if sample[2] != sample[3]:
                T2.rotate(d)
                if sample[0] != sample[1]:
                    T1.rotate(-d)
    return
    


def calc(N):
    if N == 1:
        if T1[0] == 'S':
            return 1
        return 0
    if N == 2:
        if T2[0] == 'S':
            return 2
        return 0
    if N == 3:
        if T3[0] == 'S':
            return 4
        return 0
    if N == 4:
        if T4[0] == 'S':
            return 8
        return 0


T1 = deque(list(map(NS, input().strip())))
T2 = deque(list(map(NS, input().strip())))
T3 = deque(list(map(NS, input().strip())))
T4 = deque(list(map(NS, input().strip())))

K = int(input())

sequence = deque()
for _ in range(K):
    N, d = map(int, input().strip().split())
    sequence.append((N-1, d))

# rotate = 1:시계 -1:반시계
T1.rotate
while sequence:
    N, d = sequence.popleft()
    
    my_rotate(N, d)


print(sum(list(map(calc, [1, 2, 3, 4]))))