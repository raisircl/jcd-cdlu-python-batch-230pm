def sq(num):
    return num**2

x=lambda num: num**2
print(x(5))


numbers=[1,2,3,4,5]
sq_list=list(map(lambda num:num**2,numbers))
#sq_list=list(map(sq,numbers))

print(sq_list)
