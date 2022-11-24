from datetime import datetime
from email import header

from chapter09.ex01 import DATE_FORMAT

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


try:
    with open('sensors.csv', 'rt', encoding='utf-8') as f:
        data = f.readlines() #-->
    
    result = []
    for row in data[1:]:
        row = row.strip().split(',')    #row의 참조가 변경됨. <-- CSV 표준 모듈
        row[0] = int(row[0])       #ID -> int 변환
        row[3] = float(row[3])      #VALUE -> float 변환
        row[4] = datetime.strptime(row[4], DATE_FORMAT) #<..-- pandas
        result.append(row)
        print(row)
        
    header, data = data[0].strip().split(','),result
    
    print(header)
    print("="*80)
    for row in data:
        print(row)
    #분석 가능...
        
except Exception as e:
    print(e)