def calcstep(**args):
    print(args)
    begin = args.get('begin', 0)
    end = args.get('end', 0)
    step = args.get('step', 1)
    
    total = 0
    for num in range(begin, end +1, step):
        total += num
    return total
print("3 ~ 5 =", calcstep(begin=3, end=5, step=1))
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3))

print("3 ~5 = ", calcstep(step=1, end= 5, begin=3, END=4, BEGIN=3))
print("3 ~5 =", calcstep(step=1, end=5))
print("3~5 =", calcstep(end=5))

even = {
    'begin' : 0,
    'end' : 100, 
    'step' :2
}

print(calcstep(**even))  #사전에 대한 연산자

odd = {
    **even,
    'begin' : 1
}
