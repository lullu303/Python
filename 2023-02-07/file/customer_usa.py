line_counter = 0
data_header = []

customer_usa_only_list = []
customer = None # 초기화

with open("customers.csv", "r") as customer_data:
    while 1:
        data = customer_data.readline()
        if not data : break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            # customer_list.append(data.split(","))
            customer = data.split(",")
            if customer[10].upper() == "USA" :   #10번째 인덱스칸의 값을 대문자로 변환했을 때, USA 이라면
                customer_usa_only_list.append(customer) # 그것만 usa_only_list에 저장해라.
        line_counter += 1

print("header: ", data_header)
for i in range(0,5):
    print(f"Data {i} : {customer_usa_only_list[i]}")
    
# print(len(customer_usa_only_list))
# print(len(customer_usa_only_list))  # 몇개인가? 34개

with open("customer_USA_only.csv", "w") as customer_USA_only_csv :
    for customer in customer_usa_only_list:
        customer_USA_only_csv.write(",".join(customer).strip('\n')+"\n") 
        # join : 합쳐서 문자열로 리턴 , 그 사이에 쉼표를 넣어준다.
        # ('\n')+"\n" 줄바꿈 지우고, 다시 만들기