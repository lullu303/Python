fname = input('입력할 파일의 이름: ')
f = open(fname, 'r')                            # 파일 열기
n = 1                                           # 줄 번호를 출력하기 위한 변수
l = f.readline()
while l:                                        # 읽어들일 줄이 있으면 반복 수행
    print(f'{n:3d}: {l}',end = '')    # 줄 번호와 내용을 출력
    n += 1                                      # 줄 번호를 증가시킴
    l = f.readline()                            # 다음 줄을 읽어온다
    


f.close()

print()

print('========================')
#read_file_lines()를 사용해서 처리

from file_util import read_file_lines

data = read_file_lines(fname)

for n, l in enumerate(data, 1) :
    print(f'{n:3d}: {l}')