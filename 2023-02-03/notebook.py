class NoteBook(object):
    def __init__(self, name):
        self.name = name
        self.pages = 0
        self.notes = {}

    def add_note(self, note, page_number=0) :
        if len(self.notes.keys()) < 300 :
            if page_number == 0 :
                if self.pages < 301 :
                    self.notes[self.pages] = note
                    self.pages += 1
                else:
                    for i in range(300):
                        if i not in list(self.notes.keys()):
                            self.notes[self.pages] = note
            else:
                if page_number not in self.notes.keys():
                    self.notes[page_number] = note
                else:
                    print("해당 페이지에는 이미 노트가 존재합니다.")
        else:
            print("더이상 노트를 추가하지 못합니다.")
    def remove_note(self, page_number):
        del self.notes[page_number]

    def get_number_of_all_lines(self) :
        result = 0
        for k in selt.notes.keys():
            result += self.notes[k].get_number_of_characters()
        return result

    def get_number_of_all_pages(self):
        return len(self.notes.keys())
    
    def __str__(self):
        return self.name