# 문자열에서 사용되는 연산자 : +, *
#  + : 문자열과 문자열을 연결하여 하나의 문자열로 합침
#  * : 문자열을 곱하는 수만큼 반복 생성
# str() : 문자열로 변환
Str = '안녕하세요\n'
result = Str * 3
print(result)

id = '990312-1234567'
for i in range(14):
    print(id[i],end=" ")
print()
print('---------------------------------')
print(id[0:14])  # 990312-1234567
print(id[:6]) # 990312
print(id[7:]) # 1234567
print(id[-1:])  # 마지막에서 끝까지
print(id[7:-1]) # 맨 마지막 - 1 까지
print(id[7:(7+7)]) #계산 가능
print(id[:]) # 전체