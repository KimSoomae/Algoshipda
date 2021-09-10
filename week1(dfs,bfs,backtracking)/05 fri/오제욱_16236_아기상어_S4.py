import sys; readline = sys.stdin.readline
N = int(input())
Map = [list(map(int,readline().split())) for _ in range(N)]

flag = False
for x in range(N):
    for y in range(N):
        if Map[x][y] == 9:
            shark_x = x
            shark_y = y
            flag = True
            break
    if flag:
        break

dx = [-1,0,1,0]
dy = [0,-1,0,1]
Map[shark_x][shark_y] = 0
shark = 2
shark_num = 0
tot_t = 0
def calculatedist(x,y):
    global shark
    visited = [[-1]*N for _ in range(N)]
    stack = [[x,y]]
    visited[x][y] = 0
    eatable = []
    while stack:
        tmp_stack = []
        for x,y in stack:
            for _ in range(4):
                nx,ny = x+dx[_], y+dy[_]
                if N>nx>=0 and N>ny>=0 and visited[nx][ny] == -1 and Map[nx][ny] <= shark:
                    visited[nx][ny] = visited[x][y] + 1
                    tmp_stack.append([nx,ny])
                    if 0 < Map[nx][ny] < shark:
                        #먹을 수 있다.
                        eatable.append([nx,ny])

        if eatable:
            eatable.sort(key=(lambda x: (x[0],x[1])))
            return eatable[0], visited[eatable[0][0]][eatable[0][1]]
        stack = tmp_stack[:]
    return False, False



while True:
    eatable_idx, time = calculatedist(shark_x,shark_y)
    if not eatable_idx:
        break

    tot_t += time
    #print(eatable_idx)

    shark_num += 1
    shark_x,shark_y = eatable_idx
    if shark_num==shark:
        shark_num = 0
        shark += 1
    #print(tot_t, shark,shark_num)
    Map[eatable_idx[0]][eatable_idx[1]] = 0

print(tot_t)