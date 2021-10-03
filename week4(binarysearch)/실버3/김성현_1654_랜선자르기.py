k,n= map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))
start = 1
end = max(line)
 
while(start<=end):
    mid = (start+end)//2
    cnt = 0
    for i in line:
        cnt += i//mid
    if cnt>=n: #자른 개수가 많으면 -> 더 크게잘라야함
        start = mid+1
    else:
        end = mid-1
print(end)


