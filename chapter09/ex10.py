import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = os.path.join(path, f)
        if os.path.isdir(fullpath): #디렉토리이면 다시 dumpdir 호출
            print("[%s]"%fullpath)
            dumpdir(fullpath)
        else:   #파일이면그냥 출력
            print("\t" + f)

dumpdir('.')