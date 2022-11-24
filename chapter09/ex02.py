import shutil
import os

shutil.copy("live.txt", "live2.txt")

answer = input("live2.txt를 삭제할까요? [y]/n :").lower()   #upper() => 대문자로 변환.

# y\n, n\n
#엔터만 쳤을 때 비어있는 문자열이 전달됨.
#
# answer= answer.lower(), 파이썬 문자열은 불변객체(내용 수정 불가)
print(answer)

if answer == 'y' or answer =='':
    os.remove('live2.txt')
    