# import sys 를 써야한다니...
import sys
T = int(input())
for _ in range(T):
    n = int(input())
    score = []
    for _ in range(n):
        tmp = list(map(int,sys.stdin.readline().split()))
        score.append(tmp)
    score.sort() # score 첫번째 값을 기준으로 정렬을 한다
    ans = 1
    b = score[0][1] # 맨 처음 기준은 서류심사 1등의 면접 점수이다
    for i in range(1,n):
        if b > score[i][1]: # 기준보다 면접 점수의 등수가 낮다면
            ans += 1 # 답을 하나 증가 시켜주고
            b = score[i][1] # 기준을 방금 비교해서 더 낮은 등수의 면접 점수로 바꿔준다
    print(ans)

# 인터넷 참고한 더 빠른 풀이
# import sys
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     score = [0] * (n+1)
#     for _ in range(n):
#         a, b = map(int, sys.stdin.readline().split())
#         score[a] = b
#     ans = 1
#     min_val = score[1]
#     for i in range(2,n+1):
#         if score[i] < min_val:
#             ans += 1
#             min_val = score[i]
#     print(ans)


