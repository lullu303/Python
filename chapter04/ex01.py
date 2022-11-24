numbers = [ 2, 3, 4, 5, 6, 8, 10]
numbers2 = [11,22,33,44,55,66,77,88,99]

#리스트의 요소 중 홀수의 값만 찾아 odd_list에 저장하세요
#odd_list를 출력하세요

def find_odds(numbers):
    odd_list = []
    for n in numbers:   #매개변수로 해줘야 함 => 의존하지 않게 하기 위해. numbers = 지역변수(매개변수)
        if n % 2 == 1:  #홀수 검사
            odd_list.append(n)
    return odd_list
       
odd_list = find_odds(numbers) # numbers= 전역변수 top level에서 대입
print(odd_list) 

odd_list = find_odds(numbers2)
print(odd_list)   