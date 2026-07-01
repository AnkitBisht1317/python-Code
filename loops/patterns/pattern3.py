"""
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
"""
# row = int(input("Enter the number of row : "))
# col = int(input("Enter the number of Column : "))

# for i in range(1,col+1):
#     a = i
#     for j in range(1,row+1):
#         if a>=1:
#             print(f"{a}",end = " ")
#             a = a-1
#     print() 

row = int(input("Enter the number of row : "))
col = int(input("Enter the number of Column : "))

for i in range(1,col+1):
    for j in range(i,0,-1):
        print(f"{j}",end = " ")
    print()  