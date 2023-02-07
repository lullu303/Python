# raise문 - try-except 문과 달리 필요할 때 예외를 발생시키는 코드

while True:
    value = input("변환할 정수값을 입력해주세요: ")
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("숫자값을 입력하지 않았습니다.")
        
    print("정수값으로 변환된 숫자 -" ,int(value))