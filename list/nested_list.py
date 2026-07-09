matrix = [
    [1,2,3,9,8],
    [4,5,6,7,6],
    [7,8,9,19,30],
    [7,8,9,19,30],
    [7,8,9,19,30]
]
r = len(matrix)
c = len(matrix[0])

for i in range(0,r):
    for j in range(0,c):
        print(matrix[i][j], end = " ")
    print()    

print("Upper triangle matrix : ")
for i in range(0,r):
    for j in range(0,c):
        if i>=j:
            print(matrix[i][j], end = " ")
        else:
            print("*",end = " ")
    print()            