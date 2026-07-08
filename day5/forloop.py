#for loop in python used to get item from a collection one by one
# if you implement for loop on collection then you do not need to worry about 
# the length of the collection or the index of the item in the collection
# syntax: for item in collection:
# a=[44,22,66,88,33,88,22]
# for i in a:
#     print(i)
num=int(input("Enter a number:"))
for i in range(1,11,1):
    print(f"{num}x{i}={i*num}")

#x=list(range(1,11))
#print(x)

for i in range(10,0,-1):
    print(i)