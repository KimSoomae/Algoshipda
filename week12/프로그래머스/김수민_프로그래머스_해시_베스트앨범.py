# 프로그래머스 해시 베스트앨범 - 레벨 3 김수민
from collections import defaultdict
import heapq

def solution(genres, plays):
    answer = []
    genre_play = defaultdict(int) # 장르별 플레이 수 합
    song_play = defaultdict(list) # 장르별 플레이수, 고유번호

    for i in range(len(plays)):
        genre_play[genres[i]] += plays[i]
        # 장르별로 플레이수 많은순, 고유번호 낮은 순으로 저장
        heapq.heappush(song_play[genres[i]], ((-plays[i], i), i))
    # 장르 별 플레이수 합 내림차순 정렬
    genre_play_sorted = sorted(genre_play.items(), reverse=True, key=lambda item: item[1])

    for key, value in genre_play_sorted:
        song_cnt = 0
        # 플레이수 많은 장르 순으로(같으면 고유번호 작은순), 재생수 많은 곡 2개의 고유번호 저장
        while song_play[key]:
            if song_cnt >= 2: break
            p, idx = heapq.heappop(song_play[key])
            answer.append(idx)
            song_cnt += 1
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 500, 2500]))