# 21608 상어 초등학교 - 구현 (김수민)
N = int(input())
student = []
seat = [[0] * (N + 1) for _ in range(N + 1)]
student_idx = [0] * (N * N + 1)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N * N):
    student.append(list(map(int, input().split())))
    student_idx[student[i][0]] = i
# 조건에 따라 학생 자리 배치
for i in range(N * N):
    # my_y, my_x는 학생이 배치될 자리의 인덱스. my_bin은 탐색 중인 자리에서 상하좌우로 빈 자리 개수. max_tmp는 좋아하는 학생수
    my_y = 0 ; my_x =0; my_bin = 0; max_tmp = 0
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            tmp = 0 # 좋아하는 학생 수
            case_two = 0 # 2번째 조건을 위해. 상하좌우로 빈자리 카운트
            if seat[y][x] == 0:
                for p in range(4):
                    ny = y + dy[p]
                    nx = x + dx[p]
                    if 1 <= ny <= N and 1 <= nx <= N:
                        if seat[ny][nx] == 0: case_two += 1
                        for s in range(1, 5):
                            # 좋아하는 친구가 인접해있으면
                            if seat[ny][nx] == student[i][s]:
                                tmp += 1
            # 지금 자리가 좋아하는 친구 젤 많으면 배치될 자리 업데이트
            if tmp > max_tmp:
                my_y = y ; my_x = x; my_bin = case_two; max_tmp = tmp
            # 같은 경우 두번째 조건 - 빈자리 많은 자리로 업데이트
            elif tmp == max_tmp:
                if case_two > my_bin:
                    my_y = y; my_x = x; my_bin = case_two
            # 3번째 조건은 어차피 행, 열 작은순으로 탐색하니까 고려 안해도 됨
            # 주변에 좋아하는 친구도 없고 빈자리도 없는데 자리 비어있으면
            if my_y == 0 and my_x == 0 and seat[y][x] == 0:
                my_y = y; my_x = x
    # 최종 위치에 학생 배치
    seat[my_y][my_x] = student[i][0]
anw = 0
# 만족도 계산
for i in range(1, N + 1):
    for j in range(1, N + 1):
        tmp = 0
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if 1 <= ni <= N and 1 <= nj <= N:
                # 좋아하는 학생이 인접해있으면 카운트
                if seat[ni][nj] in student[student_idx[seat[i][j]]][1:5]:
                    tmp += 1
        # 조건에 따라 만족도 합산
        if tmp >= 1:
            anw += pow(10, tmp-1)
print(anw)