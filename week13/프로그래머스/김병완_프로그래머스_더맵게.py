def solution(scoville, K):
    from heapq import heapify, heappop, heappush
    answer = 0
    heapify(scoville)
    while scoville[0] < K:
        try:
            first = heappop(scoville)
            second = heappop(scoville)
            tmp = first + (second * 2)
            heappush(scoville, tmp)
        except IndexError:
            return -1
        answer += 1

    return answer

if __name__ == '__main__':
    scoville = list(map(int, input().split()))
    K = int(input())
    solution(scoville, K)