def solution(operations):
    from heapq import heapify, heappop, heappush
    answer = []
    tmp = []
    heapify(tmp)
    tmp_max = []
    heapify(tmp_max)
    for op in operations:
        if op[0] == 'I':
            temp = int(op[2:])
            heappush(tmp, temp)
            heappush(tmp_max, (-temp, temp))
        elif op[0] == 'D':
            try:
                if int(op[2:]) == 1:
                    heappop(tmp_max)
                    tmp.pop()
                elif int(op[2:]) == -1:
                    heappop(tmp)
                    tmp_max.pop()
            except IndexError:
                pass

    if len(tmp):
        answer.append(tmp_max[0][1])
        answer.append(tmp[0])
    else:
        answer = [0, 0]
    return answer

if __name__ == '__main__':
    operations = list(map(int, input().split()))
    print(solution(operations))