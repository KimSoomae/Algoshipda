def solution(jobs):
    from heapq import heapify, heappush, heappop
    answer = 0
    now = 0
    idx = 0
    start = -1
    time = []

    while idx < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heappush(time, (job[1], job[0]))
        if len(time) <= 0:
            now += 1
            continue
        tmp = heappop(time)
        start = now
        now += tmp[0]
        answer += (now - tmp[1])
        idx += 1

    answer = int(answer / len(jobs))
    return answer

if __name__ == '__main__':
    jobs = list(map(int, input().split()))
    print(solution(jobs))