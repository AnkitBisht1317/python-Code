n = int(input("Enter the number : "))
fact = 1
result = 0
for i in range(1,n+1):
    fact = fact*i
    result = result + i/fact

print(result)