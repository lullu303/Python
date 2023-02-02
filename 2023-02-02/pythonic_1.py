# 파이썬 스타일 코드
colors = [ 'red', 'blue', 'green', 'yellow' ]

# 방법 1
result = ''
for s in colors :
        result += s
print(result)

# 방법 2
result = ''.join(colors)
print(result)
