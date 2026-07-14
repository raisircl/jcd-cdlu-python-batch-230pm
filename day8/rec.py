# when a function calls itself then that function
# is known as recursive function 
# and the process is known as recursion.
def factorial(n): 
    if n == 1:
        return 1 
    else:
        return n * factorial(n - 1)
              #5 * 24
              #4 * 6
              #3 * 2
              #2 * 1
x=factorial(5) # 120

print(x)    