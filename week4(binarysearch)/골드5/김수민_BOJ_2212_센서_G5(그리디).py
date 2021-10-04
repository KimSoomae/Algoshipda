# BOJ 2212 센서 - 그리디 G5 김수민
N = int(input())
K = int(input())
arr = list(set(map(int, input().split()))) # set으로 중복 제거
arr.sort()
tmp = 0; cnt = 1; anw = 0
tmp_list = [] # 가장 간격이 큰 뒷 센서의 인덱스 저장
n = len(arr)
if K == 1: # 집중국 한개 설치하면 센서 마지막-처음이 간격
    anw = arr[-1] - arr[0]
elif K >= n: # 집중국을 센서보다 같거나 많이 세울 수 있으면 거리는 0
    anw = 0
else:
    while cnt < K: # 최대 간격인 센서 담기 - 나중에 거기 포함안되게 집중국 설치하기 위해
        for i in range(1, n):
            if i not in tmp_list: # 아직 추가 안됐고
                if arr[i]-arr[i - 1] > tmp: # 최대 간격이면
                    tmp = arr[i] - arr[i - 1]
                    tmp_idx = i
        cnt += 1; tmp = 0
        tmp_list.append(tmp_idx) # 인덱스 담기
    tmp_list.sort()
    start = 0
    # 시작 구간(시작~ 최대 간격 인덱스 전까지)
    anw += arr[tmp_list[0]-1] - arr[0]
    start = tmp_list[0]
    # 중간 구간(설치된 집중국~다음 집중국 전까지 거리 계산)
    for i in range(1, len(tmp_list)):
        anw += arr[tmp_list[i]-1] - arr[start]
        start = tmp_list[i]
    # 끝나는 구간
    anw += arr[-1] - arr[start]
print(anw)