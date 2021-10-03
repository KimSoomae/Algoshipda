import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) //2
    value = 0

    for i in range(N):
        if trees[i] > mid:
            value += trees[i] - mid
        
    if value >= M:
        start = mid + 1
    else:
        end = mid -1
print(end)


