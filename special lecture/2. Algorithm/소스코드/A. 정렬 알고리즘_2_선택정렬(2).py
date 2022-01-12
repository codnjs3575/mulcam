## 선택 정렬 2 (완전 ver)
import random
## 함수
def selection_sort(arr):
    n = len(arr)
    for cy in range(n-1):
        min_idx = cy
        for i in range(cy+1,n) :
            if arr[min_idx] > arr[i] :
                min_idx = i
        arr[cy] , arr[min_idx] = arr[min_idx] , arr[cy]
    return arr

## 전역 변수
data_arr = [random.randint(100,200) for _ in range(8)]

## 메인 코드
print(f'정렬 전 : {data_arr}')

data_arr = selection_sort(data_arr)

print(f'정렬 후 : {data_arr}')