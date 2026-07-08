'''
use a loop inside another loop
1.
**
**
**
2.
*
**
***
****
*****
'''
i=1
while i<=5: # i used for row
    j=1
    while j<=i: # j used for column
        print("*",end="")
        j+=1
    print() # to print new line after each row
    i+=1
