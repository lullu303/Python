def kwargs_test(a, b, *args, **kwargs) :
    print(a + b + sum(args))
    print(kwargs)

# kwargs_test(3,4,5,6,7,8,9, first=3, second=4, third=5)

def isNumEven(a) :
    if a % 2 == 0 :
        print(f"{a}는 짝수")
        return
    else :
        print(f"{a}는 홀수다")
isNumEven(3)