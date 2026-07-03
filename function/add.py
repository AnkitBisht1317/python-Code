first = int(input("Enter the first number : "))
second = int(input("Enter the second number : "))
sum = 0
def add(first,second):
    global sum # agar gobal ko local varibale ki trha use kre to use global sum krke hi use kr skte hai.
    sum = first + second
add(first, second)
print(sum)

## in python we sotre function inside list and also call function
l = [1,2,3,add]
l[-1](2,5)
print(sum)



# second method 
# def add(first, second):
#     return first + second

# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))

# sum = add(first, second)
# print(sum)