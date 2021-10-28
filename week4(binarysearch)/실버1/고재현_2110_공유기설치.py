def binary_search(wifi, start, end):
    while start <= end:
        mid = (start + end) // 2
        cur_house = wifi[0]
        cnt = 1

        for i in range(1, len(wifi)):
            if wifi[i] >= cur_house + mid:
                cur_house = wifi[i]
                cnt += 1

        if cnt >= c:
            global ans
            start = mid + 1
            ans = mid
        else:
            end = mid - 1



n, c = map(int, input().split())
wifi = [0] * n
for k in range(n):
    wifi[k] = int(input())
wifi.sort()
ans = 0
start = 1
end = wifi[-1] - wifi[0]
binary_search(wifi, start, end)
print(ans)