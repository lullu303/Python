line_counter = 0
data_header = []
customer_list = []

with open("customers.csv") as customer_data:
    while 1:
        data = customer_data.readline()
        if not data : break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            customer_list.append(data.split(","))
        line_counter += 1

print("header: ", data_header)
for i in range(1,10):
    print(f"Data {i} : {customer_list[i]}")
print(len(customer_list))