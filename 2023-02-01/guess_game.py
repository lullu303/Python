print("Guess game 입니다~~^^")

import random
game = random.randint(1,100) #랜덤하게 숫자를 추출

count = 0

while True: 
    count +=1

    guest_input = input("숫자를 입력해주세요: ")

    guest_input_int = int(guest_input) #int로 형변환

    if game == guest_input_int : 
        print(f"정답입니다! 입력한 숫자는 {guest_input_int}, {count}만에 맞추셨습니다!")

    elif game < guest_input_int :
         print(f"숫자가 너무 큽니다! 입력한 숫자는 {guest_input_int}, 임의의 숫자는 {game} 입니다")
        
    elif game > guest_input_int :
        print(f"숫자가 너무 작습니다!입력한 숫자는 {guest_input_int}, 임의의 숫자는 {game} 입니다.") 
            
   
