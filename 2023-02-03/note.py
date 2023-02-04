# 노트북 프로그램 만들기
class Note(object) :
    def __init__(self, contents):
        self.contents = contents

    def get_number_of_lines(self) :
        return self.contents.count("\n")
    
    def get_number_of_characters(self) :
        return len(self.contents)

    def remove(self):
        self.contents = "삭제된 노트입니다."

    def __str__(self) :
        return self.contents