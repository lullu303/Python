def calcscore(name, *score, **option):
    print(name)
    total=0
    for s in score:
        total += s
        
        print("총점: ", total)
        if(option['avg'] == True) : #option get('avg'.True)
            print("평균: ", total/len(score))
            
calcscore("홍길동", 88, 99, 77, avg=True)
calcscore("고길동", 99, 88, 95, 85, avg=False)
calcscore("고길동", 99, 88, 95, 85)

# calcscore("고길동", 99, 85, avg=False, 88, 95) => 에러