from functools import reduce

def product(n1,n2):
    "Product of two numbers"
    return n1*n2

f= reduce(product,range(1,6))

print(f"Fact is {f}")
