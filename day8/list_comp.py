x=[4,2,1,5,6,2,66,22]

y=[i**2 for i in x]
data=[f"{i} even" if i%2==0 else f"{i} odd" for i in x]


print(data)
