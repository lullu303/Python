i, j = 0, 0

while i<6:
    j=0
    while j<6:
        if(j<i):
            print('*', end ='')
        j+=1
    i+=1
    print()