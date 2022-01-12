## 함수
def open():
    global count
    print(f'박스를 엽니다.')
    count -= 1
    if count == 0:
        print(f'** 반지를 넣습니다**')
        print('박스를 닫습니다.')
        return
    open() # count가 0이 아니라면 호출
    print('박스를 닫습니다.') # 호출된 뒤 돌아와서 박스를 닫습니다.
    return # 돌아가기
    
## 전역 변수
count = 3
## 메인 코드
open() 