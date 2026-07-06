#enter mrp of a book print net price after 10% discount if mrp >=500 other wise give 5% discount
mrp=float(input("Enter the MRP of the book: "))
dis=0
if mrp>=500:
    dis=mrp*10/100
else:
    dis=mrp*5/100

net_price=mrp-dis
print(f"MRP={mrp}, Discount={dis}, Net Price={net_price}")

#Assignment 1: enter sale price and cost price of a product and print profit or loss
#Q2. enter 2 nos print which one is biggest
#Q3. enter a  number and print whether it is even or odd
#Q4. enter a number and print whether it is positive or negative
