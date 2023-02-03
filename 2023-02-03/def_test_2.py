# 함수 만들기


# for문을 사용하여 A학급의 평균 점수를 구해보세요

class_A = [70,60,55,75,95,90,80,80,85,100]

def class_avg(*args):
    

    for i in args :

        total = 0
        total = total + class_A
        avg = total / 10

    return total

class_avg()

# TypeError: class_avg() missing 1 required positional argument: 'class_A'
# UnboundLocalError: cannot access local variable 'total' 
#                      where it is not associated with a value