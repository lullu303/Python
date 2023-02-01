print("Guess game 입니다~~^^")

import random
for i in range(1):
    game = random.randint(1,100) #랜덤하게 숫자를 추출

guest_input = input("숫자를 입력해주세요: ")

guest_input_int = int(guest_input) #int로 형변환
if i == guest_input_int : 
     print(f"정답입니다 {guest_input_int, game}")

elif i > guest_input_int :
    print(f"숫자가 너무 큽니다 {guest_input_int, game}")
    
elif i < guest_input_int :
    print(f"숫자가 너무 작습니다 {guest_input_int, game}")

   
