import json
data = {'name': '홍길동', 'birth': '0525', 'age' :30} #사전을 my import.json으로 저장

with open('myinfo.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False) #false: 아스키가 아닌 데이터도 있다.

json_str = json.dumps(data, indent=4, ensure_ascii=False)
print(type(json_str))
print(json_str)