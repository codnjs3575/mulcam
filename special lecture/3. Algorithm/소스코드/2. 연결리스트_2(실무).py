# 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def print_node(start) :
    current = start
    print(current.data,end=' ')

    while current.link != None:
        current = current.link
        print(current.data,end=' ')
    print()

def insert_node(find_data,insert_data): #find_data 앞에 insert_data 추가
    global memory, head, current, pre_node

    # case 1. 첫 노드(head) 앞에 삽입 
    if find_data == head.data :
        node = Node()
        node.data = insert_data
        node.link = head
        print(head)
        head = node
        return
    
    # case 2. 두번째 노드 이후 삽입
    else :
        # current가 find_data인지 찾기
        current = head # head에서 시작

        while current.link != None:
            pre_node = current # current를 pre에 넣고
            current = current.link # current를 다음으로 이동

            if current.data == find_data: # 삽입처리
                node = Node()
                node.data = insert_data
                node.link = current
                pre_node.link = node
                return
        
        # case 3. 마지막에 추가 (없는 값 앞에 추가)
        node = Node()
        node.data = insert_data
        current.link = node
        return

def delete_node(delete_data):
    global memory, head, current, pre_node
    # 첫 노드(head)를 삭제할 때
    if delete_data == head.data :
        current = head
        head = head.link
        del(current)
        return
    # 두번째 이후를 삭제
    current = head
    while current.link != None:
        pre_node = current # 지금 값을 미리 pre_node에 저장
        current = current.link
        if current.data == delete_data:
            pre_node.link = current.link
            del(current)
            return
    
def find_node(find_data):
    global memory, head, current, pre_node

    current = head
    if current.data == find_data:
        return current
    while current.link != None :
        current = current.link
        if current.data == find_data:
            return current
    return Node() # 빈 노드 생성 후 리턴


# 전역 변수
memory = []
head,current,pre_node = None,None,None
data_arr = ['다현','정연','쯔위','사나','지효'] # 값만 바꿔 사용하면 됨

# 메인 코드
node = Node()
node.data = data_arr[0]
head = node # 중요
memory.append(node)

# node 생성
for data in data_arr[1:] : # head를 제외하고 끝까지
    pre_node = node # 앞에 있는 node값을 pre에 넣기
    node = Node() 
    node.data = data
    pre_node.link = node
    memory.append(node)

print_node(head)

# 다현 앞에 화사 넣기
insert_node('다현','화사') 
print_node(head)

# 사나 앞에 솔라 넣기
insert_node('사나','솔라')
print_node(head)

# 채원 앞에 문별 넣기
insert_node('채원','문별')
print_node(head)

# '화사' (head)(첫 노드) 삭제
delete_node('화사')
print_node(head)

# '쯔위' (중간 노드) 삭제
delete_node('쯔위')
print_node(head)

# '채원' (없는 값) 삭제
delete_node('채원')
print_node(head)

f_node = find_node('정연')
print(f_node.data)

f_node = find_node('솔라')
print(f_node.data)

# 없는 값 찾기 (None 출력)
f_node = find_node('채원')
print(f_node.data)