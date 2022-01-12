# 데이터 삽입 : enQueue(인큐) (rear + 1하고 데이터 삽입)
# 데이터 추출 : deQueue(디큐) (front + 1하고 데이터 추출)
# 첫 번째 데이터 : front(머리)
# 마지막 데이터 : rear(꼬리)
# 큐가 비어있는 상태 : front == rear

## 함수


## 전역 변수
front = rear = -1
SIZE = 5
queue = [None] * SIZE



## 메인 코드
#enQueue
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'
print(f'queue: {queue}')

#deQueue
front += 1
data = queue[front]
queue[front] = None
print(f'제거할 데이터: {data}',end=' ')
print(f'queue: {queue}')

front += 1
data = queue[front]
queue[front] = None
print(f'제거할 데이터: {data}',end=' ')
print(f'queue: {queue}')

front += 1
data = queue[front]
queue[front] = None
print(f'제거할 데이터: {data}',end=' ')
print(f'queue: {queue}')