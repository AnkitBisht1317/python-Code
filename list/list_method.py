L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,5]

print(L.count(5))
L.sort()
print(L)

L1 = L.copy()
L1.append(20)
L.append(122)
print(L)
print(L1)


L2 = [[1,2], [3,4]]

L3 = L2.copy()

L3[0].append(100)

print(L2)
print(L3)