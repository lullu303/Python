from datetime import datetime
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

now = datetime.now()

#dattime -> 문자열 변환
now_str = datetime.strftime(now, DATE_FORMAT)
print(now_str)

#문자열 -> datetime 변환
str_date = "2022-08-31 11:32:27"
s_date = datetime.strptime(str_date, DATE_FORMAT)
print(type(s_date), s_date)