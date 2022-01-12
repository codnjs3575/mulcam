## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if ((rear+1) % SIZE == front) :
        return True
    else :
        return False

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (rear == front) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('queue full!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('queue Empty!')
        return None
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('queue Empty!')
        return None
    return queue[(front+1) % SIZE]

## 전역 변수
SIZE = 5
queue = [ None for _ in range(SIZE)]
front = rear = 0 # 일반 큐와 다른 점 

## 메인 코드
enQueue('화사'); enQueue('솔라'); enQueue('문별');
enQueue('휘인'); enQueue('채원')
print('출구<---', queue , '<--입구')

deQueue()
print('출구<---', queue , '<--입구')
print(f'삭제 예정 : {peek()}')

deQueue()
print('출구<---', queue , '<--입구')
print(f'삭제 예정 : {peek()}')

enQueue('아이유')
print('출구<---', queue , '<--입구')