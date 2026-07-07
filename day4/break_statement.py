# break statement tranfer the control outside the loop
# cause of break in loop become unconditional death of loop
# it is used to exit from loop in emergency situation
'''
Syntax:
while condition:
    statement1
    statement2
    if condition:
        break   -
....           <-
....        
'''
#enter a number and check whether it is prime or not
num=int(input("Enter a number: "))
i=2
while i<num: #conditional death of loop when i and num become equal
    if num%i==0:
        break; # unconditional death of loop when num is divisible by i
    i=i+1
if num==i:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

'''
Dry Run:
num    i    Condition    num%i==0    Output
5      2    2<5 T        5%2==0 F    i=3
5      3    3<5 T        5%3==0 F    i=4
5      4    4<5 T        5%4==0 F    i=5
5      5    5<5 F        Loop Ends   
Output: 5 is a prime number
9    2    2<9 T        9%2==0 F    i=3
9    3    3<9 T        9%3==0 T    Loop Ends

Output: 9 is not a prime number

'''

# print all prime numbers between 1 to 100