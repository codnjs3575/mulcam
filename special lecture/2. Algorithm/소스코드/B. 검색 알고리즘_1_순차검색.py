import random

## 함수
def Seq_search(arr,fData):
    pos = -1
    size = len(arr)
    for i in range(size):
        if arr[i] == fData:
            pos = i
            break
    return pos

## 전역 변수
SIZE = 10
data_arr = [random.randint(1,99) for _ in range(SIZE)]
find_data = data_arr[random.randint(0,SIZE-1)]

## 메인 코드
print(f'배열 --> {data_arr}')
print(f'찾는 값 --> {find_data}')

position = Seq_search(data_arr,find_data)
if position == -1 :
    print(f'{find_data}가 없습니다.')
else :
    print(f'{find_data}가 {position+1}번째에 있습니다.')