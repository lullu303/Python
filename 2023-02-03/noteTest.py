from note import Note
from notebook import NoteBook

good_sentence = """행복의 문이 하나 닫히면 다른 문이 열린다. 그러나 우리는 종종 닫힌 문을 멍하니 바라보다가
우리를 향해 열린 문을 보지 못하게 된다. -헬렌켈러"""

note_1 = Note(good_sentence)
print(note_1)
good_sentence = """Stay hungrn stay foolish - steave jobs"""

note_2 = Note(good_sentence)
geeod_sentence = """바보같고, 멍청하고, 생각없이, 마음을 비우는 연습이 필요해 -베네딕트 컴버비치"""

note_3 = Note(good_sentence)
wise_saying_notebook = NoteBook("명언노트")
wise_saying_notebook.add_note(note_1,1)
wise_saying_notebook.add_note(note_2,2)
wise_saying_notebook.add_note(note_3,3)
print(wise_saying_notebook.get_number_of_all_pages())
print(note_3)
note_3.remove()
print(wise_saying_notebook)
print(note_1)
print(note_2)
print(note_3)

# NameError: name 'good_sentece' is not defined. Did you mean: 'good_sentence'?