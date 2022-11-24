import json

with open('myinfo.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

    print(type(data))
    print(data)
with open('myinfo.json', 'r', encoding='utf-8') as f:
    json_str = f.read() #전체 읽기
    data = json.loads(json_str)

    print(type(data))
    print(data)