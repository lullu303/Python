f = open('data5.txt', 'w')      # 5파일을 쓰기 모드로 연다.
for _ in range(5):
    n = input('정수를 입력하세요: ') #n = 문자열 txt모드이기 때문에
    f.write(n)                  # 입력된 값을 문자열로 쓰기
    f.write('\n')               # 값을 쓴 후 줄바꿈하기
f.close()