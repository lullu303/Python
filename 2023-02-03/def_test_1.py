# 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수


def identified_number(a) :
    if a % 2 == 1 :
        print(f"{a} 는 홀수다!")

    elif a %2 == 0 :
        print(f"{a} 는 짝수다!")

identified_number(0)