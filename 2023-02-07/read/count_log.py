# f = open("count_log.txt", 'w', encoding="utf8")
# for i in range(1,11):
#     data = "%d 번째 줄이다. \n"%i
#     f.write(data)

# f.close()

# with open("count_log.txt", 'a', encoding="utf8") as f:
#     for i in range(1,11):
#         data = "%d번째 줄이다.\n"%i
#         f.write(data)   # 기존에 있던 파일에 이어서 작성됨.

with open("count_log.txt", 'w', encoding="utf8") as f:
    for i in range(1,11):
        data = "%d번째 줄이다.\n"%i
        f.write(data)   # 기존에 있던 파일을 갈아엎고 작성됨