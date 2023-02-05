# 함수 만들기


# for문을 사용하여 A학급의 평균 점수를 구해보세요

class_A = [70,60,55,75,95,90,80,80,85,100]

def class_avg(*agrs):
     total= 0
     for i in args :
        total = total + i
        avg = total / 10
     return avg
     print(avg)

class_avg()

# TypeError: class_avg() missing 1 required positional argument: 'class_A'
# UnboundLocalError: cannot access local variable 'total' 
#                      where it is not associated with a value
