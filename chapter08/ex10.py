try:
    f = open('hello.txt', 'rt', encoding='utf-8')
    s = f.read(5)    #문자열로 처리 / 5글자를 읽어라.(rt) | 5byte(rb)
    print(s)

    s = f.read(5)
    print(s)

    
    f.close()
except Exception as e :
    print(e)