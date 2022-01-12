ARRAY_LENGTH = 5  # 배열의 행과 열 크기(고정)

def replaceData(numData): # numData	2차원 정수 배열
    retData = [] # 조건에 따라서 전처리된 2차원 배열
    for num in numData:
        arr = []
        for n in num :
            if n <= 0 :
                n = 0
                arr.append(n)
            elif n > 100 :
                n %= 100
                arr.append(n)
            else :
                arr.append(n)
        retData.append(arr)
    return retData

# 2x2 크기의 배열의 최대합을 구한다.
def getMaxSum(numData): # 요구 사항에 맞춰 처리된 2차원 정수 배열
    maxSum = 0 # 최대합
    global ARRAY_LENGTH
    for i in range(0,ARRAY_LENGTH-1):
        cnt = 0
        while True :
            if cnt == 4:
                break
            Sum = numData[i][cnt]+numData[i][cnt+1]+numData[i+1][cnt]+numData[i+1][cnt+1]
            if maxSum <= Sum :
                maxSum = Sum
            cnt += 1
    return maxSum

## 전역 변수 선언 부분
numData =[] # 5x5 배열
ARRAY_LENGTH = 5 # 배열의 행과 열 크기(고정)

def main() :
        global numData

        loadData() # 2차원 배열 읽어오기

        ## 원본 출력
        print(' ----- 초기 배열 -----')
        printData()

        # 1. 데이터 치환 작업
        numData = replaceData(numData)
        print(' ----- 치환 후 배열 -----')
        printData()

        # 2. 최대 합 구하기.(2x2 크기)
        maxSum = getMaxSum(numData)
        print('최대 영역의 합: %d' % maxSum)

       
## 함수 선언 부분
def  loadData() : # 데이터 불러오기
    global numData

    ###########
    # 제공 데이터 세트 1 
    # 5x5 숫자 배열. 
    ###########
    numData = \
    [
        [ 5, -7, -5, 100, 73 ],
        [ 36, 69, 90, 233, 7 ],
        [ 49, 85, 556, 34, 43 ],
        [ 124, -59, -86, 54, 52 ],
        [ 233, 43, 8, 78, -0 ]
    ]
    
    

def printData() :
        for i in range(0, ARRAY_LENGTH) :
                for k in range(0, ARRAY_LENGTH) :
                        try :
                                print("%5d" % numData[i][k], end='')
                        except :
                                pass
                print()
        print('--------------------------------------')

## 메인 함수 호출 ##
if __name__ == "__main__" :
    main()