s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])

print(s1.union(s2))

print((s1 | s2))    # 합집합

print((s1 & s2))    # 교집합

print((s1 - s2))    # 차집합