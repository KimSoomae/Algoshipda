x = int(input())

arr = [0 for _ in range(x+1)]
for i in range(x+1):
    if i in [0,1]: arr[i] = 0
    else:
        if i%2 == 0 and i%3 == 0:
            h = min(arr[i//2]+1,arr[i//3]+1,arr[i-1]+1)
            arr[i]=h
        elif i%2 == 0: arr[i] = min(arr[i//2]+1,(arr[i-1]+1))
        elif i%3 == 0: arr[i] = min(arr[i//3]+1,(arr[i-1]+1))
        else: arr[i] = arr[i-1]+1
    #print(i,arr[i])

print(arr[-1])