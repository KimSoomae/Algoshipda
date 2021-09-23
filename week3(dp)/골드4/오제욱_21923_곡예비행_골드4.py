import sys; readline = sys.stdin.readline
R, C = map(int,readline().split())
Inf = -float('inf')
updp = []
dwdp = []

#dp 테이블 2개 필요함
# Indexing 헷깔리닌까 그냥 테두리 처리
for _ in range(R):
    sub = list(map(int,readline().split()))
    updp.append([Inf]+sub[:])
    dwdp.append(sub[:]+[Inf])

updp.append([Inf]*(C+1))
dwdp.append([Inf]*(C+1))

# updp -> 상승 비행일 때 r,c에 도착하는 최대값
# dwdp -> 도착 점에서 r,c에 상승비행할 떄 도착하는 최대값
for c in range(1,C+1):
    for r in range(R-1,-1,-1):
        if c == 1 and r == R-1:
            continue
        nc = C-c
        updp[r][c] += max(updp[r+1][c],updp[r][c-1])
        dwdp[r][nc] += max(dwdp[r+1][nc],dwdp[r][nc+1])



# r,c에서 updp[r][c]와 dwdp[r][c]의 합이 최대인걸 고르면 됨
# 테두리 문제로 인덱싱이 조금 다르다.
max_v = Inf
for r in range(R):
    for idx in range(C):
        tmp = updp[r][idx+1] + dwdp[r][idx]
        # print(r,idx,tmp)
        max_v = max(max_v,tmp)


# print(updp)
# print(dwdp)

print(max_v)