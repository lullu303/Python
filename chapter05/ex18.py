from unittest import result


def sum_nums(*numbers): #positional arg로 처리될 때 튜플로 처리됨.
    result = 0
    for n in numbers:
        result += n
    return result
print(sum_nums(10,20,30))   #10,20,30 인자들의 합을 출력
print(sum_nums(10,20,30,40,50) )    #10,20,30,40,50 인자들의 합을 출력

n_list = [1, 10, 40, 45, 80]
print(sum_nums(*n_list))

print(n_list)   #list 하나가 전달
print(*n_list)  #펼쳐서 호출 (5개의 매개변수가 space로 구분되어서 출력)
                #JS: arr = [...arr1, ...arr2]
n_list2 =[ * n_list, 45, 66]
print(n_list2)
