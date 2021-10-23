# 14889 스타트와 링크[삼성SW역략테스트 기출, 조합] 실버3 김수민
def cal(cnt, start, team, n):
    global anw
    if cnt == team:
        start = list(map(int, path[0:team]))
        set1 = set(start)
        set2 = set(member)
        # 차집합
        link = list(set2 - set1)
        # 각 팀 멤버들의 능력치 계산
        t = 0 ; t2 = 0
        for i in range(team):
            for j in range(team):
                t += S[start[i]][start[j]]
                t2 += S[link[i]][link[j]]
        anw = min(abs(t-t2), anw)
        return
    # 조합 구하기 - dfs돌때 start갑을 i로 넘겨줘서 중복 방지
    for i in range(start, N):
        if visit[i]: continue
        visit[i] = 1
        path[cnt] = str(i)
        cal(cnt + 1, i, team, N)
        visit[i] = 0


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
member = list(range(0,N))
visit = [0] * (N + 1)
path = [""] * 100
anw = 100000
cal(0, 0, N//2, N)
print(anw)