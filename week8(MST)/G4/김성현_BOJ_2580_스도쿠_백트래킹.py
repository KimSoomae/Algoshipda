input = open('input.txt').readline
from itertools import permutations
import time

start = time.time()

def check_garo(depth):
    if sum(board[depth]) == 45:
        return True

def check_small_grid(n): # n : 0, 1, 2 // 0일때 012, 1일때 345 2일때 678
    for r_list in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        value = 0
        for c in range(3*n, 3*n+3):
            for r in r_list:
                value += board[c][r]
        if value != 45:
            return False
    return True      

def check_sero():
    for i in range(9):
        value = 0
        for j in range(9):
            value += board[j][i]
        if value != 45:
            return False
    return True

def dfs(depth):
    
    global result
    if depth == 9:
        if check_sero():
            if not result:
                for i in range(9):
                    result.append(board[i])
                    print(*result[i])
                return
        else:
            return
    
    if depth % 3 == 0 and depth > 1:
        if check_small_grid(depth//3 - 1):
            pass
        else:
            return
    
    zero_index = [0] * 9
    zero_cnt = 0
    for i in range(9):
        if board[depth][i] == 0:
            zero_index[i] = 1
            zero_cnt += 1
    
    if zero_cnt:
        
        perm_list = list(permutations(range(1, 10), zero_cnt))
        
        for perm in perm_list:
            
            j = 0
            for i in range(9):
                if board[depth][i] == 0:
                    board[depth][i] = perm[j]
                    j += 1
            
            if check_garo(depth):
                dfs(depth+1)
            
            for i in range(9):
                if zero_index[i]:
                    board[depth][i] = 0

N = 9
board = [list(map(int, input().split())) for _ in range(9)]
result = []
dfs(0)

#--------------------------------------------------------------#

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9]  
    
    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])

    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])
    
    return promising

flag = False 
def dfs(x):
    global flag
    
    if flag: 
        return
        
    if x == len(zeros):
        for row in sudoku:
            print(*row)
        flag = True 
        return
        
    else:    
        (i, j) = zeros[x]
        promising = is_promising(i, j)
        
        for num in promising:
            sudoku[i][j] = num #
            dfs(x + 1)
            sudoku[i][j] = 0 
dfs(0)