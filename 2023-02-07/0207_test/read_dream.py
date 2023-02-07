f = open("i_have_a_dream.txt", "r") 
contents = f.read()   # 파일 읽기
# print(contents)


# print(len(contents)) # 전체 글자수 : 959
# print(len(contents.split(' '))) # 공백 기준 split해서 단어 수 세기 : 171


# -----------------------------------------------------------------------------

print(len(contents.split('\n')))    # 전체 라인 수 29

# f.close()