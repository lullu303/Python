# 중첩반복문
world_1 = "hello"
world_2 = "world"

result = [i + j for i in world_1 for j in world_2]
print(result)   # 중첩 for문

result = [i + j for i in world_1 for j in world_2 if not(i==j)]
print(result)
