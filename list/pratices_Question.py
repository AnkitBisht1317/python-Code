# to find max without using max function
L = [4,5,8,9,3,5,45,6,89,100,4,2]

max = L[0]
n = len(L)
for num in range(1,n):
    if max<L[num]:
        max = L[num]

print(f"maximun value is : {max}")

print()
# check target exits in list

def checkTarget(L1,target):
    for num in L1:
        if target == num:
            return True    
    return False
        

L1 = [4,5,8,9,3,5,45,6,89,100,4,2]
print(checkTarget(L1,45))
print(checkTarget(L1,15))
print(checkTarget(L1,5))

print()

#if target exit remove target
L2 = [4,5,8,9,3,5,45,6,89,100,4,2]

target = int(input("Enter the target value  : "))

if target in L2:
    L2.remove(target)
    print(f"List is : {L2}")
else:
    print("target does not exits")    


# remove duplicate
def removeDuplicate(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    print(result)        

L3 = [4,5,8,9,3,5,45,6,89,100,4,2,4,5,3,7,8,9,12,2,3,4,6,7,9]
removeDuplicate(L3)