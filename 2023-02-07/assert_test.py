# assert문 - 미리 알아야 할 예외 정보가 조건을 만족하지 않을 경우 예외를 발생시키는 코드

def get_binary_number(decimal_number):
    assert isinstance(decimal_number, int)
    return bin(decimal_number)
print(get_binary_number(10))
print(get_binary_number("10"))