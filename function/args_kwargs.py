def create_user(name,*skills,**extra_info):
    print(f"name : {name}")
    print(f"Skills : {skills}")
    print(f"Extra Information : {extra_info}")

create_user(
    "Ankit Bisht",
    "Pthon","Java","Flutter",
    age = 22, location = "Delhi", experience = 2 
)  


