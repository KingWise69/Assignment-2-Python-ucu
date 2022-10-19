
birthyear = 2001
def take3(name,bithyear,weight):
    today = 2022
    age = today-birthyear
    print("your age is", age )
    return age 

name = str(input("Input your name :"))
if name == "":
    name = "keron"
weight = int(input("Input your weight :"))
             
print(f"Your {name} \nYour weight is {weight}kg")