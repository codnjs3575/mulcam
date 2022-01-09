


# 1장) 스택과 큐

## 1. 스택 (Stack)

- 먼저 들어온 데이터가 나중에 나가는 형식의 자료구조 (**선입후출**)
- **입구와 출구가 동일한 형태**로 스택을 시각화 할 수 있음

<img src="./Algorithm.assets/image-20220108203945035.png" alt="image-20220108203945035" style="zoom:33%;" align='left' />

### 1) 스택 동작 예시

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - 삭제() - 삽입(1) - 삽입(4) - 삭제()

<img src="./Algorithm.assets/image-20220108205326247.png" alt="image-20220108205326247" style="zoom:50%;" align='left'/>

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - 삽입(1) - 삽입(4) - 삭제()

<img src="./Algorithm.assets/image-20220108205025201.png" alt="image-20220108205025201" style="zoom:50%;" align='left' />

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - **삽입(1)** - **삽입(4)** - 삭제()

<img src="./Algorithm.assets/image-20220108205207639.png" alt="image-20220108205207639" style="zoom:50%;" align='left'/>

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - **삽입(1)** - **삽입(4)** - **삭제()**

<img src="./Algorithm.assets/image-20220108205238734.png" alt="image-20220108205238734" style="zoom:50%;" align='left' />



### 2) 스택 동작 구현 (파이썬) 

> 1_1

```python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) #최하단 원소부터 출력
# 시간복잡도 : O(1)
```



## 2. 큐 (Queue)

- 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조 (**선입선출**)
- 큐는 **입구와 출구가 모두 뚫려 있는 터널**과 같은 형태로 시각화 할 수 있음

<img src="./Algorithm.assets/image-20220108210225463.png" alt="image-20220108210225463" style="zoom:33%;" align='left' />



### 1) 큐 동작 예시

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - 삭제() - 삽입(1) - 삽입(4) - 삭제()

<img src="./Algorithm.assets/image-20220108210405675.png" alt="image-20220108210405675" style="zoom:50%;" align='left' />



- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - 삽입(1) - 삽입(4) - 삭제()

<img src="./Algorithm.assets/image-20220108210537436.png" alt="image-20220108210537436" style="zoom:50%;" align='left'/>

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - **삽입(1)** - **삽입(4)** - 삭제()

<img src="./Algorithm.assets/image-20220108210624974.png" alt="image-20220108210624974" style="zoom:50%;" align='left'/>

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - **삽입(1)** - **삽입(4)** - **삭제()**

<img src="./Algorithm.assets/image-20220108210607581.png" alt="image-20220108210607581" style="zoom:50%;" align='left'/>



### 2) 큐 동작 구현 (파이썬)

> 1_2

```python
# 큐 (Queue) 구현을 위해 deque 라이브러리 사용
from collections import deque

queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 순서대로 출력
```

# -------------------------------------------------------------------



# 2장) 우선순위에 따른 자료구조

## 1. 우선순위 큐 (Priority Queue)

- 우선순위 큐는 **우선순위가 가장 높은 데이터를 가장 먼저 삭제**하는 자료구조
- 우선순위 큐는 **우선순위에 따라 처리하고 싶을 때** 사용
  - 예시) 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야 하는 경우

<img src="Algorithm.assets/image-20220109113107613.png" alt="image-20220109113107613" style="zoom:50%;" align='left' />



- 우선순위 큐를 **구현하는 방법**
  - 1) **리스트**를 이용하여 구현
  - 2) **힙(heap)**을 이용하여 구현



- 데이터의 개수가 `N개`일 때, 구현 방식에 따라서 시간 복잡도를 비교한 내용

<img src="Algorithm.assets/image-20220109113506340.png" alt="image-20220109113506340" style="zoom:50%;" align='left' />



- 단순히 N개의 데이터를 `heap`에 넣었다가 모두 꺼내는 작업은 정렬과 동일 (**힙 정렬**)
  - 이 경우 시간 복잡도 : **O(NlogN)**



### 1) 힙(heap)

- 힙(heap)의 특징

  - 힙(heap)은 **완전 이진 트리 자료구조**의 일종
  - 힙(heap)에서는 항상 **루트 노드(root node)를 제거**
  - **최소 힙(min heap)**
    - 루트 노드 = 가장 작은 값
    - 따라서 **값이 작은 데이터**가 우선적으로 제거

      <img src="Algorithm.assets/image-20220109113936379.png" alt="image-20220109113936379" style="zoom:33%;" align='left'/>

  

  

  - **최대 힙(max heap)**
    - 루트 노드 = 가장 큰 값
    - 따라서 **값이 큰 데이터**가 우선적으로 제거
      



### 2) 완전 이진 트리(Complete Binary Tree)

- 완전 이진 트리란 `루트(root) 노트`부터 시작하여 `왼쪽 자식 노드`, `오른쪽 자식 노드` 순서대로 데이터가 차례대로 삽입되는 트리(tree)

<img src="Algorithm.assets/image-20220109114251479.png" alt="image-20220109114251479" style="zoom:40%;" align='left'/>

### 3) 최소 힙 구성 함수 : Min-Heapify()

- (**상향식**) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치 교체

<img src="Algorithm.assets/image-20220109114445394.png" alt="image-20220109114445394" style="zoom:40%;" align='left' />

- 새로운 원소가 **삽입**될 때

  - **O(logN)**의 시간 복잡도로 힙 성질 유지

  <img src="Algorithm.assets/image-20220109114752834.png" alt="image-20220109114752834" style="zoom:40%;" align='left' />



- 기존 원소가 **제거**될 때

  - **O(logN)**의 시간 복잡도로 힙 성질 유지
    - 1 . 가장 **마지막 노드가 루트 노드의 위치**에 오도록 함

    <img src="Algorithm.assets/image-20220109114906364.png" alt="image-20220109114906364" style="zoom:40%;" align='left' />

    
    
    - 2. 이후 루트 노드에서부터 **하향식**으로 (더 작은 자식 노드로 ) Heapify() 진행
    
    <img src="Algorithm.assets/image-20220109115212664.png" alt="image-20220109115212664" style="zoom:40%;" align='left'/>



### 4) 힙 정렬 구현 예제 (파이썬) (우선순위 큐 라이브러리 활용)

```python
import sys
import heapq #힙 라이브러리
input = sys.stdin.readline

def Heap_sort(iterable): #리스트/튜플 등
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)): # 내림차순 : 꺼낼 때, - 이용
        result.append(heapq.heappop(h))

    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = Heap_sort(arr)

for i in range(n):
    print(res[i]) # 오름차 순
```


# -------------------------------------------------------------------

# 3장) 