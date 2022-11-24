f =open('foo.txt', 'r')     # 파일 열기

s = f.readline()            # 파일의 첫번째 줄을 읽어온다 =>AAA\n
print(s, end='')            # 이 줄을 출력한다

s = f.readline()            # 파일의 두번째 줄을 읽어온다 =>BBB\n
print(s, end='')            # 이 줄을 출력한다

s = f.readline()            # 파일의 세번째 줄을 읽어온다 =>CCC\n
print(s, end='')            #이 줄을 출력한다

s = f.readline()            # 파일의 세번째 줄을 읽어온다 =>'' (비어있는 문자열) | bool = False
print(s, end='')            #이 줄을 출력한다


f.close()                   #파일을 닫는다.