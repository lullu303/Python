# 단어 통계 정보 산출

# log 디렉토리가 없으면 log 디렉토리를 생성한다.
# [1] log 디렉토리가 있지만, log/count_log.txt 파일이 없으면 파일을 생성한다
# [2] log/count_log.txt 을 append mode 로 파일을 open 한다.
# [3] random과 datetime 모듈을 import 한다
# [4] range(1,11) 함수를 사용하여 for loop 돌면서, 현재시간(timestamp)을 string으로 변환하여
# stamp에 저장한다.
# [5] 랜덤한 값에 100000 곱해서 value에 저장한다.
# [6] stamp와 value를 파일에 write() 한다.

import os
import random # [3]
from datetime import datetime

count_log = []
stamp = None #초기화
value= None

os.mkdir("log") # make directory => log directory가 생김

try : 
    if not os.path.isdir("log") : # log라는 디렉토리가 존재하지 않으면
        os.mkdir("log") # 만들어라

    if os.path.isdir("log") : # log라는 디렉토리가 있으면
        f = open("log/count_log.txt","w")  # 파일을 생성해라

        for i in range(1,11) :
            ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # [4] string으로 변환
            count_log.txt.append(stamp) # count_log에 저장하라

        value = random() * 100000   # [5]

        f = open("count_log.txt", 'w')
        contents = stamp + value    # [6]

except FileExistsError :
    print("파일이 있는데 만들었음")      

    