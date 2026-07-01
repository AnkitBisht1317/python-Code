"""
1 2 3 4 5 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5 
"""
row = int(input("Enter the number of row : "))
col = int(input("Enter the number of Column : "))

for i in range(1,col+1):
    for j in range(1,row+1):
        if i>=j:
            print(f"{j}",end = " ")
    print()   