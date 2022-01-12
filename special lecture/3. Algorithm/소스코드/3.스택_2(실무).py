## 함수
def  isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE -1) :
        return True
    else :
        return False

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False

def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print('stack full')
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('stack empty')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data
    
def peek(): # 데이터를 빼진 않고 가장 위에있는 값 
    global SIZE, stack, top
    if (isStackEmpty()):
        print('stack empty')
        return None
    return stack[top]

## 전역
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
push('커피1')
push('커피2')
push('커피3')
push('커피4')
push('커피5')
print(stack)
push('커피6') # 출력 : stack full 
ret_data = pop()
print(f"pop: {ret_data}")
print(f'stack : {stack}')

ret_data = pop()
print(f"pop: {ret_data}")
print(f'stack : {stack}')

ret_data = pop()
print(f"pop: {ret_data}")
print(f'stack : {stack}')

print(f'다음 : {peek()}')