try:

    with open('hello2.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        print(data)
except Exception as e:
    print(e)

print("=====================")


try: 
        with open ('hello.txt', 'r', encoding='utf-8') as f:
            pass
except Exception as e:
    print(e)