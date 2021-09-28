import sys
# sys.stdin = open('김병완_1946_신입사원_S1.txt', 'r')
input = sys.stdin.readline
for tc in range(int(input())):
    N = int(input())
    cnt = 1
    DtoI = [0] * (N + 1)
    for i in range(1, N + 1):
        Docu, Interview = map(int, input().split())
        DtoI[Docu] = Interview

    min_rank = DtoI[1]
    for rank in range(2, N + 1):
        if min_rank < DtoI[rank]:
            continue
        min_rank = DtoI[rank]
        cnt += 1
    print(cnt)