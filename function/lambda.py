## without lambda funtion
def cube(x):
    return x**3

def transfrom(f,L): ## higer order function
    output = []
    for i in L:
        output.append(f(i))
    print(output)

L = [1,2,3,4]
transfrom(cube,L)

## we use lambda function with Higer order function
## with lambda function 
def transfrom(f,L): ## higer order function
    output = []
    for i in L:
        output.append(f(i))
    print(output)

L = [1,2,3,4]
transfrom(lambda x : x**3,L)
