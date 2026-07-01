email  = input("Enter your email: ")
password = input("Enter your password: ")

if email == "ankitbisht805727@gmail.com" and password == "1234":
    print("WelCome")
elif email == "ankitbisht805727@gmail.com" and password != "1234":
    print("Invalid password, please try again!")
    password = input("Enter your password again : ")
    if password == "1234":
        print("Welcome, finally!")
    else: 
        print("Invalid password again, your chance is over!")    
else:
    print("Invalid email and password")

