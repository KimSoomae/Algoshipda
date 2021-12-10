# 프로그래머스 스택/큐 다리위를 지나는 트럭 - 레벨2 김수민
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    move = deque()
    # 0만큼 채워놓고, 0을 빼고 넣으면서 이동
    for _ in range(bridge_length):
        move.append(0)
    # arrive: 도착한 트럭 개수, now_weight: 현재 다리에 있는 트럭 무게 합(sum 연산 시간 줄이려고), idx = 들어가야될 트럭 인덱스
    arrive = 0; now_weight = 0; idx = 0
    N = len(truck_weights)
    while True:
        # 다 도착했으면 break
        if arrive == N:
            break
        # 마지막 트럭 도착
        fin = move.pop()
        # 0이 아닌 진짜 트럭이면
        if fin != 0:
            arrive += 1
            now_weight -= fin
        # 들어가야 될 트럭이 들어가도 무게가 감당 가능하면
        if now_weight + truck_weights[idx] <= weight:
            move.appendleft(truck_weights[idx])
            now_weight += truck_weights[idx]
            if idx < N - 1:
                idx += 1
        # 못들어가면 0을 넣어서 이동
        else: move.appendleft(0)
        # 시간 경과
        answer += 1

    return answer

# print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))