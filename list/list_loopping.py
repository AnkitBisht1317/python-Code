L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

i = 0
n = len(L)
total = 0
#first way to apply for loop
for j in range(0,n):
    total = total + L[j]    
print(total) 

#best method using for loop
for num in L:
    print(f"{num}")
 
# if reverse 
for num in L[::-1]:
    print(f"{num}")

#by the help of enumerate  
for index, num in enumerate(L):
    print(f"Index = {index+1} : Value = {num} ")  