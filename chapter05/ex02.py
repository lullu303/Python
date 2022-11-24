numbers2 = [11,22,33,44,55,66,77,88,99]

#최소값을 찾아서 인덱스를 리턴하는 find_min() 함수 작성
def find_min(numbers2):
    #numbers2에서 최솟값을 ㅊ자아 그 인덱스를 리턴
    min_value = numbers2[0]
    min_index = 0
    
    for ix, n in enumerate(numbers2):
        if n < min_value:   #새로운 최소값이면
            min_value = n
            min_index = ix
            
    return min_index
print(numbers2)
min_index = find_min(numbers2)
print(min_index, numbers2[min_index])