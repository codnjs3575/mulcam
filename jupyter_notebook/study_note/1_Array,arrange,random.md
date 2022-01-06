> 01/06 ~ 
>
> www.numpy.org
# 1. numpy 모듈 선언

- 새로운 노트북을 실행한 경우 다시 선언해야 함

   ```python
    import numpy as np
   ```
   ```python
     np.__version__ #'1.20.3'
   ```



## 2. Array 정의 및 사용
- 시퀀스 데이터(리스트,튜플 등)로부터 배열 생성
- http://numpy.org/doc/stable/reference/arrays.html

## 1. array 생성 (object)

`형식` : arr_obj = np.array(seq_data)

```python
data1 = [1,2,3]
data1  # [1,2,3]
```




## 2. array 크기 확인 : shape





## 3. array 자료형 확인 : dtype





## 4. 배열 생성

### 1) 범위 지정해 배열 생성 : np.arnage() 함수
### 2) 범위 지정해 배열 생성 : linspace() 함수
### 3) 특별한 형태의 배열 생성
- a. 모든 요소가 0인 배열 생성
- b. 모든 요소가 1인 배열 생성
- c. 대각 요소가 1인 배열 생성
	- np.eye
	- np.identity
	- np.empty
### 4) 배열의 데이터 타입 변환 : astype() 함수
- 문자열 배열을 숫자형 배열로 변환
- 실수형 배열을 정수형 배열로 변환
- 숫자형 배열을 문자열 배열로 변환

### 5) 배열의 broadcasting




# 3. 난수 배열 생성

## 1. random.rand([d0, d1, ..., dn])
## 2. random.randint([low,] high [,size])





# 4. Array 연산

## 1. 기본 연산
## 2. 통계를 위한 연산