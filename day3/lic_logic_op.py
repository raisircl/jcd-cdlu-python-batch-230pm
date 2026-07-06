#logical operator - and
age=int(input("Enter the age of the person: "))
if age>=18 and age<=45: #10, 30, 80
    print("Eligible for LIC insurance")
else:
    print("Not eligible for LIC insurance")