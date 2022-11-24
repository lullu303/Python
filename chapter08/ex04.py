try:
    b = 2/0
    a= 1 + 'hundred'
except ZeroDivisionError:
    print('0으로 나누는 오류')
except TypeError:
    print('지원되지 않은 연산자를 사용하는 오류')
except Exception as e:      #보편적인 예외처리 기능
    print('error: ', e)
    print('나눗셈과 연산자를 다시 확인하세요')