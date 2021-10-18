# SWEA 5658 [모듸 SW 역량테스트] 보물상자 비밀번호
from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    s = input()
    Q = deque()
    tmp = []; cnt = 0
    for ss in s:
        Q.append(ss)
    # 보물상자 한 변씩 총길이 // 4 길이만큼 담기
    while cnt < N//4:
        for i in range(0, N, N//4):
            tmp_s = ''
            for j in range(i, i + N//4):
                tmp_s += Q[j]
            # 16진수 -> 10진수 변환
            tmp.append(int(tmp_s,16))
        # 시계방향회전 - 맨 뒤에거를 앞으로 푸쉬해서 하나씩 밀기
        back = Q.pop()
        Q.appendleft(back)
        # 중복 제거
        tmp = list(set(tmp))
        # 한변에 있는 글자 길이만큼 돌면 원래로 돌아오니까
        cnt += 1
    # 내림차순 정렬 후 K번째 수 출력
    tmp.sort(reverse=True)
    print(f'#{tc} {tmp[K-1]}')
