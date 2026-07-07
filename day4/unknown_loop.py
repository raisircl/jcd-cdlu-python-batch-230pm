# enter a number and count its digits
num=int(input("Enter a number: "))
x=0
while num>0:
    x=x+1
    num=num//10
print("Number of digits:",x)

'''
Dry Run:
num    Condition    x    num//10
1234    1234>0 T    1    1234//10 = 123
123     123>0 T     2    123//10 = 12
12      12>0 T      3    12//10 = 1
1       1>0 T       4    1//10 = 0
0       0>0 F       Loop Ends

Output: Number of digits: 4

'''

#1. enter a number and print sum of its digits
#2. enter a number and print reverse of the number
#3. enter a number and print its palindrome or not
#4. enter a number and print its Armstrong or not
#example: 153  1**3 + 5**3 + 3**3 = 153
#5. enter and number and print its binary equivalent
#6. enter a number and print it in words
#example: 1234 One Two Three Four