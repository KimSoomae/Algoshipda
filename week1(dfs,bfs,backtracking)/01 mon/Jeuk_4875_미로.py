dx = (-1,0,1,0)
dy = (0,-1,0,1)

def bfs():
    global anw, stack
    while stack:
        tmp_stack = []
        for x,y in stack:
            for _ in range(4):
                nx, ny = x + dx[_], y + dy[_]
                if N>nx>=0 and N>ny>=0 and Map[nx][ny] != 1:
                    if Map[nx][ny] == 3:
                        anw = 1
                        return
                    tmp_stack.append([nx,ny])
                    Map[nx][ny] = 1
        stack = tmp_stack[:]



for tc in range(1,10+1):
    N = 16
    Map = []
    stack = []
    anw = 0
    for _ in range(N):
        tmp = list(map(int, input()))
        Map.append(tmp)
        if 2 in tmp:
            stack.append([_,tmp.index(2)])

    Map[stack[0][0]][stack[0][1]] = 1
    bfs()
    print(f'#{tc} {anw}')
