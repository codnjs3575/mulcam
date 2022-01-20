# Week01

## Day1

### variable1
2021-12-20 변수
1. 값이 저장된 메모리의 위치를 가리키는 레퍼런스다
2. 값의 형에 따라서 고정되지 않고, 동적으로 자료 유형을 매핑해서 사용
   (type 검사)(자료형 지정 x)(동적 타이핑)
   자바: int x 처럼 변수에 대한 type를 고정시켜야 함
3. 변수는 이름을 가지고 있다
4. 변수에는 다른 값을 저장할 수 있다.(값 변경 가능)(2번과 같은 내용)
5. 변수는 선언이 필요없다.

### variable2
변수 이름(명명 규칙)
1. 대소문자 구분 : C언어 기반 (X와 x는 다름)
2. 영문자,숫자 혼용 가능하지만 숫자 먼저 사용 불가능
3. 공백 사용 불가능
    snake 형태) std_name
    camel 형태) stdName
4. 예약어 사용 불가능
    import keyword
    keyword.kwlist

### variable3
포맷 코드 사용
방법 1. print("문자열", 변수)
방법 2. 포맷 코드
      형식) print("서식" % 값)
      형식) print("문자열 %d 문자열" % 변수)

 %d : 정수
 %f : 실수
 %s : 문자열
 %c : 문자 1개
 %o : 8진수
 %x : 16진수
 %% : % 표현


## Day2
### 1. DataType
파이썬이 처리하는 자료형 (data type)
정수(integer)(int) : (2진수, 8진수, 10진수, 16진수)
실수(float) : (3.14)(1.2e3)
문자열(String)(str) : (' ')(" ")
불린(bool) : (True)(False)


형변환 (type 변환)
1.str() : 문자열로 변환
print("str(a):",type(str(a)))

str1 = str(123)
str2 = str(3.14)

2.int(문자열) : 정수형으로 변환
print(int(b),":",type(int(b)),"\n")
print("int(str1):",int(str1))


3. float(문자열) : 실수로 변환
print("float(str2):",float(str2),"\n")
### 2. input
### 3. operator
**지수 연산자 예제**
x= 3
y = 3 * x**2
print(y,"\n")

**관계 연산자 예제 : >, <, >=, <=, ==, !=**
result = 100 > 10
print(result,"\n") # True

**논리 연산자 : and, or, not**
a = int(input("a: "))
a = 100
print(a < 10 or a > 20)
print(a==100,"\n")

**비트연산자 : bit ( &, |, ^, ~, <<, >> )**
print("True & True : ",True & True)
print("True & False : ",True & False)
print("True | False : ",True | False)
print("False | False : ",False | False)
print(~a)
print(a>>1)
print(a>>2)
print(a<<1)

### 4. transDecimal

```python
print('2진수 변환 : bin()')
print(bin(11)) # 10진수 -> 2진수
print(bin(0b0011)) # 2진수 -> 2진수
print(bin(0o03)) # 8진수 -> 2진수
print(bin(0xff)) # 16진수 -> 2진수
print("")

print('8진수 변환 : oct()')
print(oct(11)) # 10진수 -> 8진수
print(oct(0b11011)) # 2진수 -> 8진수
print(oct(0xff)) # 16진수 -> 8진수
print("")

print('16진수 변환 : hex()')
print(hex(0b10101)) #2진수 -> 16진수
print(hex(0o75)) #8진수 -> 16진수
print("")
```

### 5. 제어문

## Day3
### 1. if
### 2. for

```python
# 정해진 횟수만큼 반복하는 반복문
# 형식 : for 변수 in 리스트/범위 :
#             반복문
for name in ['apple', 'banana', 'melon'] :
    print(name)
print("----------------------------------------")
# range(시작값, 끝값+1)
# range(끝값+1) : 0~끝값
# range(시작값, 끝값+1, 간격) : 시작값부터 끝값까지 간격만큼 띄어서 출력
for num in range(10) : #0~9까지 (총 10개)
    print(num)
print("----------------------------------------")
for num in range(1,10) : #1~9까지 (총 9개)
    print(num)
print("----------------------------------------")
for num in range(1, 10, 2):  # 1~9까지 2 간격으로 출력
    print(num)
print("----------------------------------------")
for num in [1,3,5,7,9] : #리스트 사용
    print(num)
print("----------------------------------------")
for num in range(10, 0, -2):  # 10에서 1까지 -2 간격으로 출력
    print(num)
print("----------------------------------------")
```

### 3. 난수



## Day4
### 0. example

### 1. in

```python
# in / not in
# 문자열 내에 특정한 문자열이 포함되어 있는지 확인
# 결과 : True / False
```

### 2. String

```python
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
```

```python
# len() : 문자열 길이 반환
len_str = len(str)

# count() : 문자열 내에 들어있는 특정 문자(열)의 개수 반환
print('< count() >')
check_str = 'o'
count_str = str.count(check_str)
print('%s은 %d개' % (check_str,count_str))

# .find(찾을문자[, start [,end] ]) : 문자열 내에서 특정 문자(열)이 존재하면
#                    문자열의 시작 위치를 반환하고, 존재하지 않으면 -1 반환
print('< .find() >')
find_str = email.find('naver')
find_str2 = email.find('naver',15)
find_str3 = email.find('@',5,11)
print(find_str) #찾으면 인덱스를 반환
print(find_str2) #없으면 -1 반환
print(find_str3)

# .index(찾을문자[, start [,end] ]) : 문자열 내에서 특정 문자(열)의 시작 위치 반환
print('< .index() >')
index_str = email.index('naver')
index_str2 = email.index('3575')
index_str3 = email.index('@')
print(index_str) #찾으면 인덱스를 반환
print(index_str2) #없으면 -1 반환
print(index_str3)

# 문자열 분리 메소드
# split() : 구분자(공백, 세미콜론, 콜론, 콤마, ...)를 기준으로 문자열 반환

city = cities.split(" ")

# 문자열 결합 메소드
# join() : 각 문자 사이에 특정문자(열) 삽입 후 결합
a = '-'
b = 'bb'

c = a.join('bbb')
print('a.join(bbb):',c)

c = a.join(b)
print('a.join(bb):',c)

c = a.join('1234')
print('a.join(1234):',c)

# replace() : 문자열 변경 메소드
# 전체 문자열에서 특정 문자열을 찾아서 다른 문자열로 변경
# 찾는 문자열이 존재하면 변경할 문자열로 대체 후 반환
# 찾는 문자열이 존재하지 않으면 원래 문자열 반환

lan = 'Python programming'
lan_rep = lan.replace('Python','Java')
print(lan_rep)

# 대소문자 변경 메소드
# 1. upper() : 대문자로 변경
# 2. lower() : 소문자로 변경
# 3. capitalize() : 문장의 첫 문자열의 첫 문자를 대문자로 변경
# 4. swapcase() : 문자의 첫 문자열의 첫 문자를 소문자로 변경, 나머지는 대문자
# 4. title() : 각 단어의 첫 문자를 대문자로 변경

upper_lan = lan.upper()
lower_lan = lan.lower()
capitalize_lan = lan.capitalize()
swapcase_lan = lan.swapcase()
title_lan = lan.title()

# 공백 제거 메소드
# 1. strip(): 문자열의 앞 뒤의 공백을 제거
# 2. lstrip() : 문자열의 왼쪽의 공백을 제거
# 3. rstrip() : 문자열의 오른쪽의 공백을 제거

string = '   ---python---      '
print(string.strip())
print(string.lstrip())
print(string.rstrip())

# 문자열 구성 파악
# isalpha() : 문자 여부 결과 반환 (True, False)
# isdigit() : 숫자인지 결과 반환
# isspace() : 하나의 문자에 대해서 공백여부 반환
# isalnum() : 문자 또는 숫자인지 확인
# islower() : 소문자여부
# isupper() : 대문자여분

# string.format()
# 1. '문자열:{위치인덱스}'.format(변수)
# 2. '문자열 {변수명}'.format(변수명=값)
# 3. '문자열 {위치인덱스:포맷코드}'.format(변수)

# 문자열 정렬 : 정렬 문자 < > ^
# 문자 : 왼쪽 정렬, 숫자 : 오른쪽 정렬
# 1. < : 왼쪽 정렬
string = 'python'
num = 1234
print('string: ',string)
print('left: {:-<10}'.format(string)) #왼쪽 정렬
print('right: {:->10}'.format(string)) #오른쪽 정렬
print('center: {:-^10}'.format(string)) #가운데 정렬

#  ljust(자릿수) : 왼쪽 정렬
#  rjust(자릿수) : 오른쪽 정렬
#  center(자릿수) : 가운데 정렬

print(string.ljust(10))
print(string.rjust(10))
print(string.center(10))
```

### 3. DateTime

```python
from datetime import date, datetime, timedelta

today = date.today()
year = today.year
month = today.month
day = today.day
print(f'{year}년 {month}월 {day}일')
print('----------------------------------------')
today2 = datetime.today()
current_time = datetime.now().time()
hour = current_time.hour
minute = current_time.minute
second = current_time.second
mcr_second = current_time.microsecond
print(f'{hour}시 {minute}분 {second}초 {mcr_second}')
print('----------------------------------------')
print("어제 :",today + timedelta(days=-1))
print("내일 :",today + timedelta(days=1))
print("일주일 전 :",today + timedelta(days=-7))
print("일주일 후 :",today + timedelta(days=7))
print('----------------------------------------')
current_time = datetime.now()
print("한 시간 전:",current_time + timedelta(hours=-1))
print("내일 두 시간 전:",current_time + timedelta(days=1,hours=-2))
print('----------------------------------------')
# strftime() 함수 : 날짜 형식을 문자열로 반환
print('날짜를 문자열로 변환 :',today.strftime('%Y-%m-%d %H:%M:%S'))
print('날짜를 문자열로 변환 :',today.strftime('%Y-%m-%d %I:%M:%S %p'))
print('----------------------------------------')
# strptime() 함수 : 문자열을 날짜형식으로 반환
today = '2020-06-20 17:40:20'
trans_today = datetime.strptime(today, '%Y-%m-%d %H:%M:%S')
print("문자열을 날짜로 변환 : ",trans_today)
print('----------------------------------------')
```

### 4. list

```python
# < 리스트 >
# 집합적 자료형 (여러 개의 원소를 가지는 데이터)
# 가변적 - 삽입 삭제 변경
# 다양한 형식의 데이터 : 숫자, 문자열, 논리 혼재되어 저장 가능
# 리스트 : [] 대괄호 이용하여 생성
score = [32,56,64,72,12]
print(type(score))
print(score)
print('----------------------------------------')

# 1. 리스트 생성
list1  = [] #빈 리스트로 생성
list2 = list()  #list() 함수 이용하여 리스트 생성
list3 = [1,2,3] #초기화하면서 리스트 생성
list4 = [1, 'apple', 3.5, [10,20,30], True] #서로 다른 형식의 값들도 저장 가능

print('list1: %s' % list1)
print('list2(%s): %s' % (type(list2),list2))
print('list3: %s' % list3)
print('list4: %s' % list4)
print('list4의 길이 : %s' % len(list4) )
print('----------------------------------------')

# 2.리스트 요소 출력
for l in list4:
    print(l,end=" : ")
    print(type(l))
print('----------------------------------------')

# 3. 리스트의 길이 len(리스트이름) 함수 이용하여 출력
#    리스트 인덱싱 : 리스트의 인덱스를 이용하여 접근 : 리스트명[indexId]
for i in range(0, len(list4)):
    print(list4[i], end=' : ')
    print(type(list4[i]))
print('----------------------------------------')

nums = [1,2,3]
a,b,c = nums #길이가 같다면 a,b,c에 하나씩 대응됨
print(a,b,c)
print('----------------------------------------')

# 리스트 인덱싱(indexing)
#  리스트에서 인덱스 연산자를 통하여 요소를 참조하고 접근하는 것

a = [1, 'apple', 3.5, [10,20,30], True]
print('a[0] :',a[0])  #첫번째 요소
print('a[-1] :',a[-1])  #마지막 요소
print('a[-5] :',a[-5])  #첫번째 요소
print('a[3] :',a[3]) #세번째 요소
print('a[3][0] :',a[3][0]) #세번째 요소_[0]
print('a[3][1] :',a[3][1]) #세번째 요소_[1]
print('a[3][2] :',a[3][2]) #세번째 요소_[2]
print('a[3][-1] :',a[3][-1]) #세번째 요소_[2]
print('----------------------------------------')

b = ['apple','banana','melon']
c = [a,b]
print(c)
print('c[0][3][1] :',c[0][3][1]) #20
print('----------------------------------------')
# 리스트의 슬라이싱 (slicing)
# 슬라이싱 연산 결과는 리스트 반환
# [start : end]
print(a[:])
print(a[3:])
print(a[:3])
print(a[2:4])
print(a[-1:])
print(a[:-1])

#  함수 : 함수이름()
#        함수이름()으로만 호출
#        input(), print(), len(), del() : 내장 함수
#        사용자 정의 함수

#  메소드 : 메소드이름()
#  클래스의 멤버인 객체를 통해서 사용
#  string객체이름.find()

# 리스트에서 사용되는 함수 : len() => 리스트의 길이 반환(원소의 개수)
# a = [1,2,3,4,5]
# print(len(a))

# 리스트 연산
# 1. 리스트 합치기 : +
# 2. 리스트 곱하기 : * (반복)
# 3. 리스트 내용 변경


fruits = ['apple','banana','melon']
a = [1, 'apple', 3.5, [10,20,30], True]

# 1. 리스트 합치기 : +
b = fruits + a
print("fruits + a")
print(b)
print('-----------------------------')

# 2. 리스트 곱하기 : * (반복)
c = fruits * 3
print("fruits * 3")
print(c)
print('-----------------------------')

# 3. 리스트 내용 변경
a[3]='melon'
print("a[3]='melon' => ",a)
print('-----------------------------')
a[1:3] = [10,11,12]
print("(a[1:3] = [10,11,12]) => ",a)
print('-----------------------------')
a[0] = [-1,-4]
print("(a[0] = [-1,-4]) => ",a)
print('-----------------------------')

# 리스트 복사
# 1. 얕은 복사 : 실제 리스트가 복사되지 않고 참조값(주소)만 복사
a = [1,2,3,4]
b = a
print('a:',a)
print('b:',b)

a[-1] = 100
b[0] = 0.5
print('a: %s \nb: %s'%(a,b))
print('-----------------------------')

# 2. 깊은 복사 (deep cody) : 리스트 복사본을 새로 생성하여 반환
# list() 함수 또는 copy모듈의 deepcopy() 함수 사용
# 2-1. list() 함수
a = [1,2,3,4]
c=list(a)
print('바뀌기 전 c :',c)
c[0] = 'apple'

print('바뀐 뒤 a :',a)
print('바뀐 뒤 c :',c)
print('-----------------------------')
# 2-2. copy모듈의 deepcopy() 함수
import copy

d=['a','b','c']
e = copy.deepcopy(d)
print('',e)

e[0] = 1
print('',d)
print('',e)
```

