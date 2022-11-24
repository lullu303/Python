total = 0
for i in range(1, 11):
    total = total + i
    # print('i= {}, total = {}'.format(i, total)) #파이썬의 format 메서드 호출/ 대체문자열 대신에 {}
    print(f'i = {i}, total ={total}') #f => formatting 문자열

print('1에서 10까지의 합:', total)