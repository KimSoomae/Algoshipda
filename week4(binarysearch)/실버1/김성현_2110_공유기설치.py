import sys
sys.stdin = open('input.txt', 'r')

N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)])

s = 1; e = house[-1]-house[0]
answer = 0
while s <= e :
    mid = (s+e) // 2
    now_loc = house[0]
    cnt = 1

    for loc in house:
        if loc - now_loc >= mid:
            cnt += 1
            now_loc = loc

    if cnt >= C:
        s = mid + 1
        answer = mid
    else:
        e = mid - 1

print(answer)
## answer 변수를 안쓰면 오답으로 나오는데 왜??
    
    
# 1 2 4 8 9
# 1 0 1 0 1
