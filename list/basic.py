#empty list
print([])
#1D
print([4,5,7,8,8])
#2D
print([[3,4],[76,56],[90,-1]])
#hetrogeneous
print([4,6.4,'hello',6+9j,[3,4,65]])
#type conversion
print(list('hello'))

l = [[[23,78],[6,5]],[[4,5],[89,54]]]
print(l[0][1][1])


#Slicing in python
L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(L[0:5])
print(L[5:15])
print(L[0:])
print(L[0:13:3])
print(L[0::2])

#Adding Element to the list:
L.append(18)
L.append([19,20,21,22])
L.extend([23,24,25,26])
L.extend("delhi")

L.insert(1,100)
print(L)

#update array
L2 = [1,2,3,4,5,6,7,8]
L2[1] = 100
L2[2:6] = [9,10,11,12]
print(L2)