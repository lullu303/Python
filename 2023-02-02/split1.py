items = 'zero one two three'.split()    #빈칸 기준 문자열 분리
print(items)

example = 'python, java, c'
example.split(",")  # ,를 기준으로 문자열 분리
print(example.split(","))

a,b,c = example.split(",")  # 분리된 각 값을 언패킹
print(a,b,c)
