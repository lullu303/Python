# 함수 개발 가이드라인
    # 가능하면 짧게 작성할 것
    # 함수 이름에 함수의 역할과 의도를 명확히 드러낼 것

def print_hello_world() :
    print("hello, world")
def get_hello_world() :
    return "hello, world"

# 함수의 역할
    # 하나의 함수에는 유사한 역할을 하는 코드만 포함하며, 한가지 역할을 명확히 해야 함

def add_variables(x,y) :
    # print(x,y)
    return x + y

# 함수를 만드는 경우
import math

def get_result_quadratic_equation(a, b, c) :
    values = []
    values.append(( -b + math.sqrt(b **2 - (4 * a * c))) / (2 * a))
    values.append(( -b - math.sqrt(b **2 - (4 * a * c))) / (2 * a))
    return values

print(get_result_quadratic_equation(1, -2, 1))