# 7_1
from random import randint
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1,100))

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range( i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i],array[min_index] = array[min_index],array[i]

# 측정 종료
end_time = time.time()
# 수행 시간 출력
print(f'선택 정렬 성능 측정 : {end_time -  start_time}')

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1,100))

# 기본 정렬 프로그램 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

# 측정 종료
end_time = time.time()
# 수행 시간 출력
print(f'기본 정렬 성능 측정 : {end_time -  start_time}')



# 7_2
n,k = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i] :
        # 두 원소를 교체
        a[i],b[i] = b[i],a[i]
    else : # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))



