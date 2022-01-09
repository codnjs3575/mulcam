class Node:
    def __init__(self,data,left_node,right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회 (Pre-order Traversal)
def pre_order(node):
    print(node.data,end=' ') # 1. 뿌리
    if node.left_node != None :
        pre_order(tree[node.left_node]) # 2. 왼쪽 노드
    if node.right_node != None:
        pre_order(tree[node.right_node]) # 3. 오른쪽 노드

# 중위 순회 (In-order Traversal)
def in_order(node):
    if node.left_node != None :
        in_order(tree[node.left_node]) # 1. 왼쪽 노드
    print(node.data,end=' ') # 2. 뿌리
    if node.right_node != None:
        in_order(tree[node.right_node]) # 3. 오른쪽 노드

# 후위 순회 (Pose-order Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node]) # 1. 왼쪽 노드
    if node.right_node != None:
        post_order(tree[node.right_node]) # 2. 오른쪽 노드
    print(node.data, end=' ') # 3. 뿌리

#---------------------------------------------------------------------------
n = int(input())
tree = {} # 딕셔너리 형태

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node =="None":
        left_node = None
    if right_node == "None" :
        right_node = None
    tree[data] = Node(data,left_node,right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])