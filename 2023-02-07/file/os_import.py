import os
# os.mkdir("log") # make directory => log directory가 생김
# FileExistsError: [WinError 183] 파일이 이미 있으므로 만들 수 없습니다: 'log'

if not os.path.isdir("log") : # log라는 디렉토리가 존재하지 않으면
    os.mkdir("log")