# 다음 데이터를 리스트와 딕셔너리를 사용하여 출력하세요
    # 1. 각 로우(행)을 딕셔너리로 표현한다
    # 2. 4개의 딕셔너리를 포함한 리스트를 만든다
    # 3. 각 딕셔너리의 key와 value를 출력한다

user_info = { 1:['hong kildong','hong@mail.com','010-2343-9870'],
2:['lee soonsin','lee@mail.com','010-3333-5555'], 
3:['jang younsil','jang@mail.com','010-7777-1234'], 
4:['king sejong','king@mail.com','010-4567-0987']}

# print(type(user_info)) # dict

print(user_info)

print(user_info.keys())
print(user_info.values())