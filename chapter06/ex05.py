import time
start_time = time.time()    #시작시간을 기록
print(1+2+3+4+5+6+7+8+9+10)

end_time = time.time()      #종료시간을 기록
gap = end_time - start_time
print(f'1에서 10까지의 합을 구하고 출력하는 시간: {gap:7.4f}초')