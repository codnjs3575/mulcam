# 1. 숫자 합계 내기 (10부터 1까지 합게를 구하는 예)
def add_num(num):
    if num <= 1 :
        return 1
    return num + add_num(num-1)
print(add_num(5))
print('-'* 40)

# 2. 팩토리얼
def fac(num):
    if num <= 1 :
        return 1
    return num * fac(num-1)
num = 5
print(f'{num}! = {fac(num)}')
print('-'* 40)

# 3. 우주선 카운트 다운
def count_down(num):
    if num == 0 :
        print('발사!')
    else : 
        print(num)
        count_down(num-1)

count = 5
count_down(count)
print('-'* 40)

# 4. 별 출력
def print_star(num):
    if num == 0 :
        return
    print_star(num-1)
    print('*' * num)
print_star(5)

# 5. 구구단 출력
def gugu(num,dan):
    if dan == 10 :
        return 
    print(f'{num} * {dan} = {num*dan}')
    gugu(num,dan+1)

for i in range(1,10):
    gugu(i,1)
    print()

# 6. 배열의 합 계산하기
import random

def arr_sum(arr,n):
    if n <= 0 :
        return arr[0]
    return arr_sum(arr,n+1) + arr[n]

arr = [random.randint(0,255) for _ in range (random.randint(10,20))]

print(arr)
print(f'배열 합계 --> {arr_sum(arr,len(arr)-1)}')