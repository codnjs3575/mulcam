# 함수
class tree_node():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 전역 변수


# 메인 코드
node1 = tree_node()
node1.data = '화사'

node2 = tree_node()
node2.data = '솔라'
node1.left = node2

node3 = tree_node()
node3.data = '문별'
node1.right = node3

node4 = tree_node()
node4.data = '휘인'
node2.left = node4

node5 = tree_node()
node5.data = '쯔위'
node2.right = node5

node6 = tree_node()
node6.data = '선미'
node3.left = node6

print(node1.data)
print(node1.left.data,node1.right.data)
print(node1.left.left.data,node1.left.right.data)
print(node1.right.left.data)