# 세트
    # 값을 순서 없이 저장하면서 중복을 불허하는 자료형
    # 수학의 집합과 개념적으로 유사

s = set( [ 1, 2, 3, 1, 2]) # 자기가 알아서 중복값 거름 -> 오류 없음, 그냥 무시함

type(s)

s.add(1)    # 중복불가로 추가되지 않음
print(s)

s.remove(1)
print(s)

s.add(1)    
print(s)

s.update([1,4,5,6,7])   # 리스트 추가
print(s)

s.discard(3) # 삭제
print(s)

s.clear()   # 모든 원소 삭제
print(s)