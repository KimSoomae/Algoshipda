import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)
def solution(start, end):
    if start > end:
        return

    div = end + 1 # div = N

    for i in range(start + 1, end + 1): # 1 ~ N-1까지

        if Tree[start] < Tree[i]: #루트 노드 < Tree[i]의 노드값? ---- 오른쪽 서브트리로 가는 지점을 찾는다
            div = i
            break
    solution(start + 1, div - 1) # 왼쪽 서브트리는 1~div-1의 index를 가진다.
    solution(div, end) # 오른쪽 서브트리는 div ~ end의 index를 가진다.
    print(Tree[start])



Tree = []
for line in sys.stdin:
    X = (int(line)) 
    Tree.append(X) # 개수가 정해지지 않은 입력을 받는 방법

# print(Tree) #기존
solution(0, len(Tree)-1) #후위순회 solution(첫번째 index, 끝의 index)





    