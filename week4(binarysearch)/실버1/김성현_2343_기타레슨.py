#시간초과 코드 ㅠㅠ

import sys
sys.stdin = open('input.txt')
N, M = map(int, input().split())
lesson = list(map(int, input().split()))

s = max(lesson); e = sum(lesson)

while s <= e:
    mid = (s + e) // 2

    cnt = 0
    value = 0

    for les in lesson:
        if value + les > mid:
            cnt += 1
            value = 0
        
        value += les
    
    if value:
        cnt += 1
    else:
        pass

    if cnt <= M:
        e = mid -1
    else:
        s = mid + 1

print(s)


''' 시간초과 코드

s = 1; e = sum(lesson)
res = 10**6
while s <= e:
    mid = (s+e)//2
    i = 0; cnt = 0; value = 0; values=0

    while i < N:
        value += lesson[i]

        if value == mid:
            if value > values:
                values = value
            value = 0
            cnt += 1
            pass
        
        elif value > mid:

            value -= lesson[i]
            i -= 1
            if value > values:
                values = value
            value = 0
            cnt += 1
        
        i += 1

        if i == N and value:
            if value > values:
                values = value
            cnt += 1

    if cnt > M:
        s = mid + 1

    else:
        if cnt == M:
            if values < res:
                res = values
        e = mid -1

print(res)
'''