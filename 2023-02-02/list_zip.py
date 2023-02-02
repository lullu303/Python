# zip()
    # 1개 이상의 리스트 값이 같은 인덱스에 있을 때 병렬로 묶는 함수
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a,b in zip(alist, blist) :
    print(a,b)

a , b, c = zip((1,2,3), (10,20,30), (100,200,300))
print(a,b,c)

sum2= [sum(x) for x in zip((1,2,3), (10,20,30), (100,200,300))]   # 같은 위치 값 더하기
print(sum2)