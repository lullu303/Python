def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('0으로 나누는 오류 발생')
    else:
        print('결과: ',result)
    finally:
        print('수행완료')   #예외발생여부와 상관없이 "항상"실행됨
    
print('divide(100,2) 함수 호출: ')
divide(100,2)
print('divide(100,0) 함수 호출: ')
divide(100,0)