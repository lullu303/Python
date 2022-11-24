def read_file_lines(fname): #자주쓰는코드 함수화 => 모듈 처리
    
    try: 
        with open (fname, 'r', encoding='utf-8') as f:                  #[2]
        # f =open(fname, 'r', encoding='utf-8')   #파일명 대신에 매개변수  [1]
            data = f.readlines() #strip 처리는 안해줌. 
            data = [line.strip() for line in data] #  => comprehention 사용해서 제거.
        return data
    except Exception as e:
        print('error',e)
    # finally:                                                             [1]
    #    if f:
    #        f.close()   #항상 닫히게 하고 싶음

if __name__ == '__main__' : # => 모듈 | 파일이 하나밖에 없다면 main
    data = read_file_lines('foo.txt')
    print(data)