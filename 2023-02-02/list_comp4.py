# 이차원리스트 
    # 일차원 리스트
word_1 = "Hello"
word_2 = "World"
result = [i + j for i in word_1 for j in word_2] 
print(result)

    # 이차원리스트
        # for 문 돌아가는 방법이 다름
result = [[i + j for i in word_1] for j in word_2]
print(result)
        #  for j in world_2
        #     for i in word_1 i+j