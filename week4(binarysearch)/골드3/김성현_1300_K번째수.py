import sys
sys.stdin = open('input.txt')

N = int(input())
K = int(input())


start = 0; end = K**2

while start <= end:
    mid = (start + end) //2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, mid//i)

    if cnt < K:
        start = mid+1
    else:
        end = mid -1

print(start)