# 2110 공유기 설치
# index가 아닌 공유기 간 거리를 이분탐색
# for문 돌리면서 개수를 세보고 탐색중인 거리 충족되는 개수에 따라 탐색거리 업데이트해서 재귀돌기 - 아이디어 블로그 참고함,,도저히 머리 안굴러감
def bs(minL, maxL, C):
    global anw
    # 종료조건 끝나면 리턴
    if minL > maxL:
        return
    # 최소거리, 최대거리의 중간 거리부터 탐색
    mid = (minL + maxL) // 2
    #tmp는 설치된 공유기 개수, wifi는 직전에 설치되 공유기
    tmp = 1
    wifi = house[0]
    for i in range(1, N):
        if house[i] >= wifi + mid: # 공유기 간 거리 충족하는 집은 공유기 설치
            tmp += 1
            wifi = house[i]
    # 설치되어야 하는 개수보다 적으면 간격 줄이기
    if tmp < C:
        bs(minL, mid - 1, C)
    # 많으면 간격 늘리기 (혹은 같아도 더 간격 늘릴 수 없는지 확인)
    else:
        # 같아서 더 찾는데 중간에 종료될 수도 있으니까 미리 저장
        anw = mid
        bs(mid + 1, maxL, C)

N, C = map(int, input().split())
house = []
for i in range(N):
    house.append(int(input()))
house.sort()
anw = 0
bs(1, house[N-1]-house[0], C)
print(anw)