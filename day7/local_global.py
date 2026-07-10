user="Anil" # global variable can be accessed anywhere in the program

def sayhello():
    global user # global keyword is used to access global variable inside the function
    user="John" #local variable can not be accessed outside the function
    print(f"Hello, {user}!, {globals()['user']}")
    # global variable and local variable ambiguity can be resolved using global keyword
    # prefernce is given to local variable if both have same name

sayhello()
print(user)
