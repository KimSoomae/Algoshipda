input = open('input.txt').readline


def calculate(value, target_number, i):
    if i == 0:
        return value + target_number
    if i == 1:
        return value - target_number
    if i == 2:
        return value * target_number
    if i == 3:
        if value > 0:
            return value // target_number
        else:
            return 0 - (0-value) // target_number
    
def dfs(k):
    
    global value

    if k == N:
        if value < result[0]:
            result[0] = value
        if value > result[1]:
            result[1] = value
        return
    
    target_number = Numbers[k]

    for i in range(4):
        if operator[i]:
            temp = value
            value = calculate(value, target_number, i)
            operator[i] -= 1
            dfs(k+1)
            value = temp
            operator[i] += 1

N = int(input())
Numbers = list(map(int, input().strip().split()))
operator = list(map(int, input().split()))


value = Numbers[0]
result = [0xfffff, 0]
dfs(1)

print(result[1])
print(result[0])
