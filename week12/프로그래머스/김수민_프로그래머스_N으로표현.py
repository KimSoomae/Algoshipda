# 프로그래머스 dp 레벨3 - N으로 표현
def solution(N, number):
    answer = -1
    if N == number: return 1
    dp = []

    for i in range(1, 9):
        arr = set()
        check = int(str(N) * i)
        arr.add(check)
        for j in range(0, i - 1):
            # i번 사용해서 만들 수 있는 수 = j번 사용 + N - j번 사용
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    arr.add(op1 - op2)
                    arr.add(op1 + op2)
                    arr.add(op1 * op2)
                    if op2 != 0: arr.add(op1 // op2)
        if number in arr:
            answer = i
            break
        dp.append(arr)

    return answer

print(solution(5, 12))
print(solution(2, 11))