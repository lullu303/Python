# 함수 만들기


# for문을 사용하여 A학급의 평균 점수를 구해보세요

class_A = [70,60,55,75,95,90,80,80,85,100]
args = 0

def class_avg(i, class_A=None):
     total= 0
     if class_A is None:
            class_A=[]
            class_A.append(i)
            for class_A in i :
                total = total + class_A
                avg = total / 10
     return avg
     print(avg)

print(class_avg(class_A))

# TypeError: class_avg() missing 1 required positional argument: 'class_A'
# UnboundLocalError: cannot access local variable 'total' 
#                      where it is not associated with a value
# TypeError: 'int' object is not iterable