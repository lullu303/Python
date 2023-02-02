
# 구구단
i , j = 0,0

for j in range(2,10) : 
    for i in range(1,10) : 
        if i <= j: 
            print(f'{j} * {i} = {j*i}')
        
