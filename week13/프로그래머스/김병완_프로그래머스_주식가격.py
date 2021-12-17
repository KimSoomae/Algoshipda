def solution(prices):
    from collections import deque
    answer = []
    tmp_prices = deque(prices)
    while tmp_prices:
        tmp = tmp_prices.popleft()
        inc_time = 0
        for price in tmp_prices:
            inc_time += 1
            if tmp > price:
                break
        answer.append(inc_time)
    return answer

if __name__ == "main":
    prices = list(map(int, input().split()))
    print(solution(prices))