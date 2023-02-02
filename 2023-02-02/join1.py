# 문자열로 구성된 리스트를 합쳐 하나의 문자열로 반환
colors = [ 'red', 'blue', 'green', 'yellow' ]

result = ' '.join(colors) # 공백 포함.
print(result)

result = ', '.join(colors)  # , + 공백 포함
print(result)

result = '-'.join(colors)  # - 포함
print(result)