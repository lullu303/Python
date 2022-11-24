datas = [
    "livingroom, temp,24.5",
    "livingroom,humi, 60.4",
    "bedroom, temp, 28.5",
    "bedroom,humi, 60.2"
]

#전달된 문자열 리스트 데이터를
#place, type, value 키를 가지는 사전의
# 리스트로 변환하는 함수 loae_data()를 만드세요.

def load_data(datas) :
    dict_list = []
    for line in datas:
        row = line.split(',')
        data = {
            'place' : row[0].strip(),
            'type' : row[1].strip(),
            'value' : float(row[2])
        }
        dict_list.append(data) #함수의 기본 골격
        
    return dict_list 

dict_list = load_data(datas)

print(dict_list)

for data in dict_list:
    print(data)
