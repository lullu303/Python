f =open('foo.txt', 'r')     

data = []

s = f.readline()

while s:
    data.append(s.strip())  #공백문자 : 스페이스, 탭, 엔터
    # print(s, end='')
    s = f.readline()

f.close()

print(data)