# def print_something(my_name, your_name) :
#     print("Hello ", your_name, "My name is ", my_name)

# my_name = "choco"
# your_name = "emily"
# print_something(my_name, your_name)


# print_something(your_name="chloe", my_name="emily") => 파이썬

# def asterisk_test(a,b, *args) :
#     return a + b + sum(args)

# print(asterisk_test(1,2,3,4,5))

def asterisk_test2(*args) :
    x, y, *z = args # z => list로 묶어서 한꺼번에 할당을 했다. , 언패킹하는 방법
    return x, y, z

print(asterisk_test2(3,4,5,10,20))