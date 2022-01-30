# 반드시 정렬이 되어 있어야 함
import random

## 함수
def bin_search(arr,fData):
    pos = -1
    start = 0
    end = len(arr) - 1

    while start <= end :
        mid = (start + end) // 2
        print(mid)
        if arr[mid] == fData :
            return mid
        elif fData > arr[mid] :
            start = mid + 1
        else :
            end = mid - 1

    return pos

## 전역 변수
SIZE = 10
data_arr = [random.randint(1,99) for _ in range(SIZE)]
find_data = data_arr[random.randint(0,SIZE-1)]
# find_data = 999
data_arr.sort()

## 메인 코드
print(f'배열 --> {data_arr}')
print(f'찾는 값 --> {find_data}')

position = bin_search(data_arr,find_data)
if position == -1 :
    print(f'{find_data}가 없습니다.')
else :
    print(f'{find_data}가 {position+1}번째에 있습니다.')