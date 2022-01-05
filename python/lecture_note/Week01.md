# 1. 변수와 자료형

## 1. 변수 (variable)


- 변수

   ```
   1. 값이 저장된 메모리의 위치를 가리키는 레퍼런스다
   2. 값의 형에 따라서 고정되지 않고, 동적으로 자료 유형을 매핑해서 사용
      (type 검사)(자료형 지정 x)(동적 타이핑)
      자바: int x 처럼 변수에 대한 type를 고정시켜야 함
   3. 변수는 이름을 가지고 있다
   4. 변수에는 다른 값을 저장할 수 있다.(값 변경 가능)(2번과 같은 내용)
   5. 변수는 선언이 필요없다.
   ```

  ```python
  a = [20,30,40]
  b = a[0] + 10.0 #30.0
  ```

- 포맷 코드 사용

  ```
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
  ```

  ```python
  #1 
  name,age = '홍길동',20
  print('나이: %d살' % age)
  
  #2
  tea,n = 'coffee',5
  s3 = f'나는 {tea}를 좋아합니다. 하루에 {n}잔 마셔요'
  print(s3)
  
  #3
  print((format(1.234567),'10.3f'))
  
  #4
  print('Name:{0}, Phone: {1}'.format('kim', '1234-213'))
  ```
  
  

## 2. 자료형 (data type)

- 자료형

	```
	파이썬이 처리하는 자료형 (data type)
	1. 정수(integer)(int) : (2진수, 8진수, 10진수, 16진수)
	2. 실수(float) : (3.14)(1.2e3)
	3. 문자열(String)(str) : (' ')(" ")
	4. 불린(bool) : (True)(False)

- 형변환

  - `str()` : 문자열로 변환
  
  - `int()` : 정수형으로 변환
  
    ```python
    print(int('1010',2)) #2진수로 변환 #10
    print(int('1010',8)) #8진수로 변환 #520
    print(int('1010',16)) #16진수로 변환 #4112
    ```
  
  - `float()` : 실수로 변환
  
  - `bin()` : 2진수로 변환
  
    ```python
    print(bin(11)) # 10진수 -> 2진수 #0b1011
    print(bin(0b0011)) # 2진수 -> 2진수 #0b11
    print(bin(0o03)) # 8진수 -> 2진수 #0b11
    print(bin(0xff)) # 16진수 -> 2진수 #0b11111111
  
  - `oct()` : 8진수로 변환
  
    ```python
    print(oct(11)) # 10진수 -> 8진수 #0o13
    print(oct(0b11011)) # 2진수 -> 8진수 #0o33
    print(oct(0xff)) # 16진수 -> 8진수 #0o377
    ```
  
  - `hex()` : 16진수로 변환
  
    ```python
    print(hex(0b10101)) #2진수 -> 16진수 #0x15
    print(hex(0o75)) #8진수 -> 16진수 0x3d
    ```

- 연산자

  - 산술 연산자 : `+`  `-` ` *`  `/` `//` `%`
  - 지수 연산자 : `**`
  - 관계 연산자 : `>` `<` `>=` `<=` `==` `!=`
  - 논리 연산자 : `and` `or` `not`
  - 비트 연산자 : `&` `|` `^` `~` `<<` `>>`



## 3. String

- `인덱스`

    ```python
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

- `len()` : 문자열 길이 반환

    ```python
    str = 'programming'
    
    print(len(str)) #11

- `count()` : 문자열 내에 들어있는 특정 문자(열)의 개수 반환

    ```python
    str = 'programming'
    
    check_str = 'o'
    count_str = str.count(check_str)
    
    print('%s은 %d개' % (check_str,count_str)) #o은 1개
    ```

    

- `.find(찾을문자[, start [,end] ])` : 문자열 내에서 특정 문자(열)이 존재하면 문자열의 시작 위치를 반환하고, 존재하지 않으면 -1 반환

    ```python
    email = "codnjs3575@naver.com"
    
    find_str = email.find('naver')
    find_str2 = email.find('naver',15)
    find_str3 = email.find('@',5,11)
    
    print(find_str) #찾으면 인덱스를 반환 #11
    print(find_str2) #없으면 -1 반환 #-1
    print(find_str3) #10
    ```



- `.index(찾을문자[, start [,end] ])` : 문자열 내에서 특정 문자(열)의 시작 위치 반환

    ```python
    email = "codnjs3575@naver.com"
    
    index_str = email.index('naver')
    index_str2 = email.index('3575')
    index_str3 = email.index('@')
    
    print(index_str) #찾으면 인덱스를 반환 #11
    print(index_str2) #없으면 -1 반환 #6
    print(index_str3) #10
    ```

- split() : 문자열 분리 메소드, 구분자(공백, 세미콜론, 콜론, 콤마,...) 기준



## 4. 리스트



## 5. 튜플



## 6. 세트



## 7. 딕셔너리





# 2. 모듈
# 3. 패키지
# 4. 함수
# 5. 파일 입출력
# 6. 객체와 클래스

