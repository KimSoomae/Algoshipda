import sys
sys.stdin = open('input.txt')

N = int(input())
tree = {}
for _ in range(N):
    P, L, R = input().split()    
    tree[P] = [L, R]


def front(node):
    if node == '.':
        return
    
    print(node, end="")
    front(tree[node][0])
    front(tree[node][1])

def mid(node):
    if node == '.':
        return

    mid(tree[node][0])
    print(node, end="")
    mid(tree[node][1])

def end(node):
    if node == '.':
        return

    end(tree[node][0])
    end(tree[node][1])
    print(node, end="")

front('A')
print()
mid('A')
print()
end('A')
    
    
    
    





