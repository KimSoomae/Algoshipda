def solution(citations):
    answer = 0
    citations.sort()
    N = len(citations)
    for i in range(N, -1, -1):
        cnt = 0
        idx = N - 1
        while idx >= 0 and citations[idx] >= i:
            cnt += 1
            idx -= 1
        if cnt >= i:
            return i