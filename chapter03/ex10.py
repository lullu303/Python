from unittest import result


def print_sum():    #지역변수 a 선언
    a = 100
    b = 200
    result = a+ b
    print('print_sum() 내부: ', a, '과', b, '의 합은', result, '입니다.')

a = 10
b = 20
print_sum()

print(a,b)  # a와 b는 전역변수로 바뀜.