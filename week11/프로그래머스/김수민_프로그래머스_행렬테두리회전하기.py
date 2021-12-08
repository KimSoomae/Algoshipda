# 2021 Dev Matching - 행렬 테두리 회전하기
def copy(rows, columns, arr, arr2):
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            arr2[i][j] = arr[i][j]
    return arr2
def solution(rows, columns, queries):
    answer = []
    arr = [[0]*(columns + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            arr[i][j] = (i - 1) * columns + j
    for i in range(len(queries)):
        x1, y1, x2, y2 = queries[i]
        arr2 = [[0]*(columns + 1) for _ in range(rows + 1)]
        arr2 = copy(rows, columns, arr, arr2)
        tmp = 0xFFFFFFF
        for j in range(y1, y2):
            arr[x1][j + 1] = arr2[x1][j]
            if arr2[x1][j] < tmp:
                tmp = arr2[x1][j]
        for j in range(x1, x2):
            arr[j + 1][y2] = arr2[j][y2]
            if arr2[j][y2] < tmp:
                tmp = arr2[j][y2]
        for j in range(y2, y1, -1):
            arr[x2][j-1] = arr2[x2][j]
            if arr2[x2][j]< tmp:
                tmp = arr2[x2][j]
        for j in range(x2, x1, -1):
            arr[j - 1][y1] = arr2[j][y1]
            if arr2[j][y1] < tmp:
                tmp = arr2[j][y1]
        answer.append(tmp)
    print(*answer)

    return answer


solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
solution(100, 97, [[1,1,100,97]] )