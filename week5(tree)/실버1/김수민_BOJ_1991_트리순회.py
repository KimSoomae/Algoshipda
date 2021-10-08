# 백준 1991 트리 순회 - 트리 S1 김수민
# 전위순회 - VLR 순서
def preorder(n):
    global s
    if n:
        s += n
        if L[n] != '.':
            preorder(L[n])
        if R[n] != '.':
            preorder(R[n])

# 중위순회 - LVR 순서
def inorder(n):
    global s2
    if n:
        if L[n] != '.':
            inorder(L[n])
        s2 += n
        if R[n] != '.':
            inorder(R[n])
# 후위순회 - LRV 순서
def postorder(n):
    global s3
    if n:
        if L[n] != '.':
            postorder(L[n])
        if R[n] != '.':
            postorder(R[n])
        s3 += n
N = int(input())
L = {} # 왼쪽 자식
R = {} # 오른쪽 자식
for i in range(N):
    node, child1, child2 = input().split()
    L[node] = child1
    R[node] = child2
s = '' ; s2 =''; s3 = ''
preorder('A')
inorder('A')
postorder('A')
print(s)
print(s2)
print(s3)