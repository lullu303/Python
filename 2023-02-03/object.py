class SoccerPlayer(object) :
    def __init__(self, name, position, back_number): #__init__ 이 클래스에서 사용할 변수를 정의하는 함수
        self.name =name 
        self.position = position
        self.back_number = back_number
    # self 변수는 클래스에서 생성된 인스턴스에 접근하는 예약어 - 생성된 인스턴스를 지정하는 변수
    # self를 매개변수에 반드시 넣어야 함. self가 있어야 인스턴스가 사용할 수 있는 함수로 선언됨.
    
    def change_back_number(self, new_number) :
        print("선수의 등 번호를 변경한다: : From %d to %d " % (self.back_number, new_number))
        self.back_number = new_number
    def __str__(self):
        return "Hello, My name if %s. I play i %s in center." % (self.name, self.position)