def solution(bridge_length, weight, truck_weights):
    from collections import deque
    answer = 1
    waitings = deque(truck_weights)
    onBridge = deque([0] * bridge_length)
    onBridge_weight = waitings.popleft()
    onBridge[-1] = onBridge_weight
    while onBridge_weight != 0:
        answer += 1
        tmp = onBridge.popleft()
        onBridge_weight -= tmp
        onBridge.append(0)
        if len(waitings) == 0:
            answer += bridge_length - 1
            break
        if onBridge_weight + waitings[0] > weight: continue
        onBridge_weight += waitings[0]
        onBridge[-1] = waitings.popleft()
    return answer

if __name__ == "main":
    bridge_length = int(input())
    weight = int(input())
    truck_weights = list(map(int, input().split()))
    print(solution(bridge_length, weight, truck_weights))