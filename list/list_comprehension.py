# print 1 to 10
new_list = [i for i in range(1,11)]
print(new_list)

#print square
new_list1 = [i*i for i in range(1,11)]
print(new_list1)

#even number
new_list2 = [i for i in range(1,11) if i%2==0]
print(new_list2)

# prime number
def isPrime(num):
    factor = 0
    for i in range(1,num+1):
        if num%i==0:
            factor +=1
    if factor == 2:
        return True
    return False        

new_list3 = [i for i in range(1,101) if isPrime(i) == True]
print(new_list3)