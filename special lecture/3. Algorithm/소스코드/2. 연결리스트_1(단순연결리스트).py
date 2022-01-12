## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

## 전역변수

## 메인코드
node1 = Node() # 빈 노드 생성 p.8
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2 # 정연 노드와 링크

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# 삽입
new_node = Node()
new_node.data = '채원'
new_node.link = node2.link
node2.link = new_node

# 삭제 
node2.link = node3.link
del(node3)

# 출력 : current 변수 사용
current = node1
print(current.data)

while current.link != None:
    current = current.link
    print(current.data)

