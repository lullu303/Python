# f = open ("dream.txt", "r")
# contents = f.read()
# print(type(contents))
# # print(contents)
# f.close()

with open("dream.txt", "r") as my_file:
    # contents = my_file.read()
    # print(type(contents, contents))
    i = 0
    while 1:
        line = my_file.readline()
        if not line:
            break # 읽을게없으면 종료해라
        print(str(i) + " === " + line.replace("\n", ""))
        i = i +1