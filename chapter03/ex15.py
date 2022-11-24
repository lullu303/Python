def func(shape, width=1, height=1, radius=1):   #필수인수(shape), 옵션
        if shape == 0 : #shape 값이 0이면 사각형의 면적을 반환
            return width * height
        if shape ==1 : #shape 값이 1이면 원의 면적을 반환
            return 3.14 * radius ** 2
        
print("rect area =", func(0, width=10, height=2))   #키워드 인수의 특징, 디폴트값이 있는 경우 중간에 있는 인수 생략 가능
print("circle area =", func(1, radius=5))