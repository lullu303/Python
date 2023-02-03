#데이터
names = ["Messi", "Ramos", "Ronaldo", "park", "Buffon"]
positions = ["MF", "DF", "CF", "WF", "GK"]
numbers = [10, 4, 7, 13, 1]

#전체 SoccerPlayer 코드
class SoccerPlayer(object) :
    def __init__(self, name, position, back_number) :
        self.name = name
        self.position = position
        self.back_number = back_number
    def change_back_number(self, new_number) :
        print("선수의 등 번호를 변경한다 : From %d to %d" % (self.back_number, new_number))
        # print(f"From {self.back_number} to {new_number}")
        self.back_number = new_number

    # def change_position(self, new_position) :
    #     print(f"선수의 포지션을 변경한다 {self.position} to {new_position}")
    #     self.position = new_position  

    def __str__(self):
        return "Hello, My name is %s. I play in %s in center." % (self.name, self.position)

# son = SoccerPlayer("son", "FW", 7)  #인스턴스
# print(son)
# print("현재 선수의 등번호는: ", son.back_number)
# son.change_back_number(5)
# print("현재 선수의 등번호는: ", son.back_number)

# print("현재 선수의 포지션은: ", son.position)
# son.change_position("DF")
# print("현재 선수의 포지션은: ", son.position)



#클래스 - 인스턴스
player_objects = [SoccerPlayer(name, position, number) 
for name, position, number in zip(names, positions, numbers)]
# print(player_objects[0])    #messi
# print(player_objects[1])    #ramos

# print(len(player_objects))  # 5

for i in player_objects:
    print(i)