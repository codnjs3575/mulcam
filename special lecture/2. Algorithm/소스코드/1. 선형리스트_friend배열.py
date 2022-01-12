# 함수 선언부
def add_friend(friend):
    katok.append(None)  # 빈칸 추가
    k_len = len(katok)
    katok[k_len-1] = friend

def insert_friend(n,friend):
    katok.append(None)
    k_len = len(katok)
    for i in range(k_len-1,n,-1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[n] = friend
    print(katok)

def delete_friend(n):
    k_len = len(katok)
    katok[n] = None
    for i in range(n+1,k_len):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[k_len-1])
    print(katok)

# 전역 변수부
katok = []
select = -1


## 메인 코드부
if __name__ == "__main__":
    while(select != 4) :
        select = int(input('선택: 1.추가 2.삽입 3.삭제 4.종료 => '))

        if select == 1 :
            data = input('추가할 데이터 => ')
            add_friend(data)
            print(f'친구 목록 : {katok}')
        elif select == 2:
            pos = int(input('삽입할 위치 => '))
            data = input('추가할 데이터 => ')
            insert_friend(pos,data)
            print(f'친구 목록 : {katok}')
        elif select == 3:
            pos = int(input('삭제할 위치 => '))
            delete_friend(pos)
            print(f'친구 목록 : {katok}')
        elif select == 4:
            print(f'친구 목록 : {katok}')

        else :
            print('1~4 중 하나를 입력하세요.')
            continue