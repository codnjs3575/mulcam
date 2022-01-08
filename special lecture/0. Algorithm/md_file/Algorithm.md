


# 1장) 스택과 큐

## 1. 스택 

- 먼저 들어온 데이터가 나중에 나가는 형식의 자료구조 (**선입후출**)
- **입구와 출구가 동일한 형태**로 스택을 시각화 할 수 있음

<img src="./algorithm.assets/image-20220108203945035.png" alt="image-20220108203945035" style="zoom:33%;" align='left' />

### 1) 스택 동작 예시

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - 삭제() - 삽입(1) - 삽입(4) - 삭제()

<img src="./algorithm.assets/image-20220108205326247.png" alt="image-20220108205326247" style="zoom:50%;" align='left'/>

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - 삽입(1) - 삽입(4) - 삭제()

<img src="./algorithm.assets/image-20220108205025201.png" alt="image-20220108205025201" style="zoom:50%;" align='left' />

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - **삽입(1)** - **삽입(4)** - 삭제()

<img src="./1_스택과 큐.assets/image-20220108205207639.png" alt="image-20220108205207639" style="zoom:50%;" align='left'/>

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - **삽입(1)** - **삽입(4)** - **삭제()**

<img src="./1_스택과 큐.assets/image-20220108205238734.png" alt="image-20220108205238734" style="zoom:50%;" align='left' />



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



## 2. 큐

- 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조 (**선입선출**)
- 큐는 **입구와 출구가 모두 뚫려 있는 터널**과 같은 형태로 시각화 할 수 있음

<img src="./1_스택과 큐.assets/image-20220108210225463.png" alt="image-20220108210225463" style="zoom:33%;" align='left' />



### 1) 큐 동작 예시

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - 삭제() - 삽입(1) - 삽입(4) - 삭제()

<img src="./1_스택과 큐.assets/image-20220108210405675.png" alt="image-20220108210405675" style="zoom:50%;" align='left' />



- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - 삽입(1) - 삽입(4) - 삭제()

<img src="./1_스택과 큐.assets/image-20220108210537436.png" alt="image-20220108210537436" style="zoom:50%;" align='left'/>

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - **삽입(1)** - **삽입(4)** - 삭제()

<img src="./1_스택과 큐.assets/image-20220108210624974.png" alt="image-20220108210624974" style="zoom:50%;" align='left'/>

- **삽입(5)** - **삽입(2)** - **삽입(3)** - **삽입(7)** - **삭제()** - **삽입(1)** - **삽입(4)** - **삭제()**

<img src="./1_스택과 큐.assets/image-20220108210607581.png" alt="image-20220108210607581" style="zoom:50%;" align='left'/>



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

# ---------------------------------------------



# 2장) 

