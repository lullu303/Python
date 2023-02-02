# enumerate()
    # 리스트의 값을 추출할 때 인덱스를 붙여 함께 출력하는 방법

for i, v in enumerate(['tic', 'tac', 'toe']) :
    print(i,v)

# 주로 딕셔너리형으로 인덱스를 키로, 단어를 값으로 하여 쌍으로 묶어 결과를 출력
words = 'The quick brown fox jumps over the lazy dog'.split()
print({i:j for i, j in enumerate(words)})