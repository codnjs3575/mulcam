## 함수
class tree_node():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역 변수
memory = []
root = None
name_arr = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

## 메인 코드
# 첫 노드 생성 (=루트 노드)
node = tree_node()
node.data = name_arr[0]
root = node
memory.append(node) # 없어도 됨

for name in name_arr[1:] : # ['레드벨벳','마마무','에이핑크','걸스데이','트와이스']
    node = tree_node()
    node.data = name

    current = root
    while True :
        if name < current.data:
            if current.left == None:
                current.left = node
                break # 자리 잡을 때까지 무한반복
            current = current.left

        else :
            if current.right == None:
                current.right = node
                break # 자리 잡을 때까지 무한반복
            current = current.right
    memory.append(node)

print('이진 탐색 트리 complete!!')

current = root
find_data = '마마무'

while True :
    if current.data == find_data:
        print(f'{find_data} 찾음!')
        break
    elif current.data > find_data :
        if current.left == None:
            print(f'{find_data} 없음!')
            break
        current = current.left
    else : 
        if current.right == None:
            print(f'{find_data} 없음!')
            break
        current = current.right