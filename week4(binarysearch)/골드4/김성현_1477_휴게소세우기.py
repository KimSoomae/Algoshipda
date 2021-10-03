import sys
sys.stdin = open('input.txt')

N, M, L = map(int, input().split())

location = [0] + sorted(list(map(int, input().split()))) + [L]
distance = []
for i in range(1, N+2):
    distance.append(location[i]-location[i-1])

distance = sorted(distance)

s = 1; e = distance[-1]
answer = 0
while s <= e:
    
    mid = (s+e)//2
    cnt = 0

    for dist in distance:
        if dist % mid:
            cnt += dist // mid
        else:
            cnt += dist // mid -1

    if cnt > M: 
        s = mid + 1
    else: 
        e = mid - 1
        answer = mid

print(answer)
