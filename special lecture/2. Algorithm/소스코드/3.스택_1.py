# 삽입 : push (top + 1 하고 데이터 넣기)
# 추출 : pop (데이터 빼고 top - 1)
# 가장 위의 데이터 : top (초기값 : -1)

## 함수


## 전역 변수
stack = [None] * 5
# size = 5
# stack = [None for _ in range(size)]
top = -1

## 메인 코드

# PUSH ----------------------------------
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
print(f'PUSH : {stack}')

# POP -----------------------------------
data = stack[top]
stack[top] = None
top -= 1
print('삭제된 데이터 :',data)

data = stack[top]
stack[top] = None
top -= 1
print('삭제된 데이터 :',data)

data = stack[top]
stack[top] = None
top -= 1
print('삭제된 데이터 :',data)

print(f'POP : {stack}')


