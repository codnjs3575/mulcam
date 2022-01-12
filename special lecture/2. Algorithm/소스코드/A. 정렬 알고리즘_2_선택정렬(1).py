## 선택 정렬 1 (완전 ver)
import random
## 함수
def find_min_index(arr):
    min_idx = 0
    for i in range(1,len(arr)) :
        if arr[min_idx] > arr[i] :
            min_idx = i
    return min_idx

## 전역 변수
before = [random.randint(100,200) for _ in range(8)]
after = []

## 메인 코드
print(f'정렬 전 : {before}')

for _ in range(len(before)):
    min_pos = find_min_index(before)
    after.append(before[min_pos])
    del(before[min_pos])

print(f'정렬 후 : {after}')

