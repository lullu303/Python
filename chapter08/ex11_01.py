f =open('foo.txt', 'r')     

s = f.readline()

while s:
    print(s, end='')
    s = f.readline()

f.close()