import sys
from bisect import bisect_left
sys.stdin = open('input.txt')

n = int(input())
num_list = list(map(int, input().split()))


dp = [1] * (n)

for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            # i번째 원소가 있고, i번째보다 앞에있는 모든 j번째 원소에 대해서 전자의 값이 크다면 증가하는 부분수열이 될 수 있음.
            # dp에서 모든 값의 자리를 1로 통일하였고, dp[i]번째 값은 dp[i] > dp[j]를 만족하는 조건 하에서 그 전까지의 dp[j]값의 최대값(최대 증가하는 부분수열) + 1 이 된다.
            # print(f'dp[{i}] = max(dp[{i}], dp[{j}] + 1), dp[{i}] = {dp[i]}, dp[{j}] = {dp[j]}')
            dp[i] = max(dp[i], dp[j]+1)
            #print(dp)            

print(max(dp))


# Bisect 모듈에 대한 이해
# bisect_left(arr, x) : arr가 정렬되어 있다는 가정하에 x값이 들어갈 위치를 반환한다 (무슨말이여;)

dp = [num_list[0]] #dp를 맨 처음 값으로 초기화 (앞으로)
for i in range(n):
    if num_list[i] > dp[-1]: #i번째의 원소가 맨 마지막 값보다 크다면
        dp.append(num_list[i]) #그냥 추가하면 된다.
        print(f'i = {i}, dp = {dp}')

    else: # i번째의 원소가 맨 마지막 값보다 작거나 같다면
        index = bisect_left(dp, num_list[i]) #들어가야할 값(num_list[i])이 dp에서 어디로 가야할 지 index값을 반환한다(이거맞나?)
        dp[index] = num_list[i]
        print(f'i = {i}, dp = {dp}')


print(len(dp))
