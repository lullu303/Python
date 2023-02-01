print("welcome to python age calculator!!") #인사^^

birth_year = input("태어난 년도를 입력하세요. ") #input으로 태어난 년도 입력하기

birth_year_float = float(birth_year) #input 형변환

# print(type(birth_year_float)) #type 확인

year = 2023 #연도 할당

# print(type(year)) # type 확인

final_age = year - birth_year_float +1 # 계산된 나이

if 17 <= final_age <20 : 

    print("고등학생입니다")

elif 20 <= final_age < 27: 
    
    print("대학생입니다.")

else : 
    print("학생이 아닙니다")