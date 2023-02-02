# in을 사용하여 특정 값 출력

student_info = {20140012: '남도산', 20140029:'서달미', 20150235:'사혜준', 20150098:'안정하'}

print('남도산' in student_info.values())
print('언초코' in student_info.values())

# dict() : 딕셔너리로 변환
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

los = ['ab', 'cd', 'ef']
print(dict(los))

tos = ('ab', 'cd', 'ef')    #튜플을 딕셔너리로 변환
print(dict(tos))