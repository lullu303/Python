# 리스트 컴프리헨션
    # 기존 리스트형을 사용하여 간단하게 새로운 리스트를 만드는 방법
    # 리스트와 for문을 한 줄에 사용할 수 있는 장점이 있음
    # 내부적으로 잘 구성된 메모리 사용 방식으로, 기존 for문 보다 시간 면에서 효율적인 연산을 수행

# 방법1
result = []
for i in range(10):
    result.append(i)
print(result)

# 방법2
result = [ i for i in range(10)]
print(result)

# 필터링
    # 방법1
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)
print(result)

    # 방법2
result = [i for i in range(10) if i % 2 == 0]
print(result)

result = [i if i %2 == 0 else 10 for i in range(10)]
print(result)