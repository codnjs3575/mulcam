# 5_1
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i],array[min_index] = array[min_index],array[i]

print(array)

# 5_2
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]: # 왼쪽 칸이 작으면 왼쪽으로 한 칸 이동
            array[j],array[j-1] = array[j-1],array[j]
        else :
            break

print(array)

