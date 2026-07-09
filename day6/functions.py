# Function - Set of instructions under a name 
# It always ready to perform a task when it is called
# Functions help in code reusability and modularity
# Functions used devide the problem into small small solutions
# syntax of function:
# def function_name(parameters):
#     # function body
#     return value
def sayhello(name="Guest"):
    print(f"Hello {name}")

def biggest(a, b):
    if a > b:
        return a
    else:
        return b

def result(hindi, eng, math, sci, sst):
    total = hindi + eng + math + sci + sst
    percentage = (total / 500) * 100
    return total, percentage

def greet(name="Guest", age=25):
    print(f"Hello my name is {name}, I am {age} years old.")

def facttorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


def fun(num):
    num=10
    print(f"The address of Num: {num} is {id(num)}")


x=100
fun(x)
print(f"The address of X: {x} is {id(x)}")   


# sayhello()

# n1=10
# n2=30
# big=biggest(n1, n2)
# print(f"Biggest number between {n1} and {n2} is {big}")

# t=0
# p=0
# t,p=result(90, 80, 70, 60, 50)
# print(f"Total marks: {t} and Percentage: {p}%")

# greet("John", 30)

# num=5
# f=facttorial(num)
# print(f"Factorial of {num} is {f}")

# call by value and call by reference 
# in python arguments always passed by reference 
# but it behaves like call by value for immutable data types 
# and call by reference for mutable data types

def display(lst):
    print(f"List: {lst} and Address of List: {id(lst)}")
    lst.append(100)
    print(f"List after modification: {lst} and Address of List: {id(lst)}")

numbers=[1,2,3,4,5]
print(f"List before function call: {numbers} and Address of List: {id(numbers)}")
display(numbers)
print(f"List after function call: {numbers} and Address of List: {id(numbers)}")