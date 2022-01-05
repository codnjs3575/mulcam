# 파일 입출력

## 1. 파일 생성 (open)

- `형식` : `객체이름 = open(생성할 파일명,파일 열기 모드)`

  - r : 읽기모드 , 기본값

  - w : 쓰기 모드

  - r+ : 읽기/쓰기 겸용 모드

  - a : 쓰기 모드, 기존에 파일이 있으면 이어서 씀 (append)

    

  - t : 텍스트 모드, 텍스트 파일 처리, 기본값

  - b : 이진 모드, 이진 파일 처리

- 주소

    1. `절대주소` : 직접적인 경로 입력, 존재하지 않는 디렉터리에 생성하는 경우 에러 발생함

       ex. 주소 입력
    
       ```python
       f = open('/Users/chaewon/python/list_num.txt','w')
       ```
    
    2. `상대주소` : 파일 이름만 씀
    
       ex. 파일이름 입력
    
       ```python
       f = open('list_num.txt','r')
       ```
    
        ex. 변수 입력
    
       ```python
       file_name = 'list_num.txt'
       f = open(file_name,'w')
       ```
    
       

## 2. 파일에 데이터 넣기 (write)

- `형식` : `객체이름.write(데이터)`
-  예시

```python
f = open('file1.txt','w',encoding='utf-8')

data = 'hello!'
f.write(data)
f.close()
```





## 3. 파일 내용 읽기 (read)

- `형식` : `객체이름 = open (파일명, 'r')`

- 예시

  - readline()
    - 방법 1
    
      ```python
      f = open('test.txt','r')
      str = f.readline() #첫번째 라인(행) 1개 읽어오기
      f.close()
      ```
  
    - 방법 2
    
      ```python
      f = open('test.txt','r')
      whiel True :
        line = f.readline()
        if not line:
          break
         print(line,end="")
      f.close()
      ```
      
      
      
      
    
  - readlines()
    
      : 리스트로 반환) 한 행이 리스트의 요소가 됨
      
      - 방법 1
      
        ```python
        f = open('test.txt','r')
        lines = f.readlines()
        print(lines)
        f.close()
        ```
  
      - 방법 2
      
        ```python
        f = open('test.txt','r')
        for line in f : #readlines() 자동 수행
          print(line,end="")
        print()
        f.close()
        ```
  
  
  - read() 
  
      ```python
      f = open('test.txt','r')
      data = f.read()
      print(data)
      f.close()
      ```
  
      
## 4. 파일 검색 위치 설정 (seek)

- `형식` : `seek(offset, whence)`

  ​		`offset` = 상대 위치 (시작 위치로부터 열의 위치)

  ​		`whence` = 위치 (0: 시작 위치, 1: 현재 위치, 2: 끝 위치)

- 예시

  ```python
  f = open('test.txt','r')
  
  f.seek(0,0) # 0행 0열
  f.seek(3,0) # 0행 3열
  f.seek(6,0) # 0행 6열
  f.seek(10,0) # 0행 10열
  f.seek(0,2) # 파일의 마지막 위치
  f.seek(14,0) # 한글은 못 읽어옴 (2바이트씩 끊어서 불러와야 함)
  
  line = f.readline()
  print(line)
  f.close()
  ```



### - 4-1) 파일 검색하기

```python
f = open('test.txt','r')
data = f.read()
value = input('검색 값 입력 : ')

if value in data:
  print('exist')
 else :
  print('not exist')
  
f.close
```



## 5. 파일 내용 추가 (append) 

- `형식` : `객체이름 = open(파일명, 'a')`

- 예시

	```python
	f = open('test.txt','a')
	
	append_data = 'Python Programming\n\n'
	
	f.write(append_data)
	f.close()
	```



## 6. close() 자동수행 (with)

- `형식`
  
   ``` 
   with open(파일명, 열기모드) as 파일객체이름 :
        수행 코드들
   ```

- `예시`

	```python
	file = 'test.txt'
	data = 'hello! it\'s a good day'
	
	with open(file,'a') as f:
	  f.write(data)
	```





## 7. OS 모듈

### 1. mkdir

```python
import os

os.mkdir('log') # 폴더 생성, 기존에 생성되어있는 폴더를 또 생성할 때 오류 발생 -> os.path 사용
```



### 2. 폴더 삭제(shutil)

```python
import shutil

shutil.rmtree('log') # 폴더 삭제
```



### 3. 기존 디렉터리 확인 (os.path)(isdir)

```python
import os
import os.path as pa

if not pa.isdir('log'):
  os.mkdir
else :
  print('already exist')
```



### 4. 디렉터리 목록 보기 (walk)

```python
import os

print(os.walk('/Users/chaewon/python'))
for dir_name, sub_dir, fnames in os.walk('/Users/chaewon/python'):
  print(dir_name)
  print(sub_dir)
  print(fname)
```



### 5. 디렉터리 존재 여부 확인 (exists)

```python
import os.path as pa

print(pa.exists('/Users/chaewon/python')) # 폴더가 있는지 확인 True/False
print(pa.isfile('/Users/chaewon/python')) # 파일인지 확인 True/False
```



### 6. 디렉터리 삭제 및 크기 확인

```python
import os

os.remove('/Users/chaewon/python') # 폴더 삭제

print(os.path.getsize('/Users/chaewon/python')) # 크기 확인
```



### 7. 파일 압축 및 풀기

```python
import zipfile as z

# 파일 압축
new = z.ZipFile('/Users/chaewon/python')
new.write('/Users/chaewon/Documents/멀티캠퍼스/파이썬/PythonStudy/PythonStudy/Week03 (0103~0107)/Day1(0103)/fileIO/test.txt',
        compress_type=z.ZIP_DEFLATED)
new.close()

# 압축 파일 풀기
ext = z.ZipFile('/Users/chaewon/Documents/멀티캠퍼스/파이썬/PythonStudy/PythonStudy/Week03 (0103~0107)/Day1(0103)/fileIO/log.zip','r')
ext.extractall('/Users/chaewon/Documents/멀티캠퍼스/파이썬/PythonStudy/PythonStudy/Week03 (0103~0107)/Day1(0103)/fileIO/')
ext.close()
```



### 8. 로그 파일 작성

```python
import os
import datetime,random

isdir = os.path.isdir('log')
ext = os.path.exists('log')

print(isdir)
print(ext)

if not os.path.isdir('log'):
    os.mkdir('log')

#로그기록용 텍스트 파일 생성
if not os.path.exists('log/countlog.txt'):
    f = open('log/countlog.txt','w',encoding='utf-8')
    f.write('기록시작\n')
    f.close()

#로그 기록
with open('log/countlog.txt','a',encoding='utf-8') as f :
    for _ in range(10):
        stamp = str(datetime.datetime.now())
        value = random.random() * 100
        log_line = stamp + '\t' +str(value)+'값 생성\n'
        f.write(log_line)
```



### 9. 이진 파일

​	: 글자가 아닌 비트 단위로 의미가 있는 파일 

​	: 그림/음악/동영상/엑셀/한글/실행(exe) 파일 등등..



- 이진파일 읽고 쓰기 (복사)

	```python
	# 읽기 : open('이진파일이름','rb')
	# 쓰기 : open('이진파일이름','wb') # write()
	# read(1) : 1바이트씩 읽기
	
	b_in = open('/Users/chaewon/Desktop/스크린샷 2022-01-03 오전 9.32.36.png','rb')
	b_out = open('/Users/chaewon/Desktop/tmp/스크린샷 2022-01-03 오전 9.32.36.png','wb')
	
	while True:
	    str_in = b_in.read(1)
	    if not str_in : #파일의 끝: 더이상 읽을 데이터가 없음
	        break
	    b_out.write(str_in)
	b_in.close()
	b_out.close()
	```
	
	

### 10. Pickle 

```python
# pickle 파일
# 메모리에 로딩된 객체나 정의된 클래스를 파일로 저장하여 사용

import pickle

# pickle.dump() : 객체(리스트형태) 저장
f = open("list.pickle",'wb')
result = [1,2,3,4,5]
pickle.dump(result,f)
f.close()

#pickle.load() : 객체 로딩
f = open("list.pickle",'rb')
result2 = pickle.load(f)
print(result2)
result2.append(100)
print(result2)
f.close()
```

