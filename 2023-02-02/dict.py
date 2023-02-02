# 딕셔너리 - 자바: 해시 맵
    # 파이썬에서 많이 사용하는 자료구조

student_info = {20140012: '남도산', 20140029:'서달미', 20150235:'사혜준', 20150098:'안정하'}
print(student_info[20140012])

type(student_info) #dict

student_info[20150125] = '김진우'   # 재할당
print(student_info[20150125])

print(student_info)

print(student_info.keys())  # 딕셔너리의 키만 출력
print(student_info.values())    # 딕셔너리의 값만 출력
print(student_info.items())   # 딕셔너리의 키와 값을 쌍으로 출력