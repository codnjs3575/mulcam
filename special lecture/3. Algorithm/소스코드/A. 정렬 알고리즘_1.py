import random
## 함수
def find_min_index(arr):
    min_idx = 0
    for i in range(1,len(arr)) :
        if arr[min_idx] > arr[i] :
            min_idx = i
    return min_idx


## 전역 변수
# test_arr = [55,88,33,77]
test_arr = [ random.randint(0,99) for _ in range(10)]

## 메인 코드
print(test_arr)
min_pos = find_min_index(test_arr)
print(f'최솟값 {test_arr[min_pos]}은 {min_pos+1}번째에 있습니다')

