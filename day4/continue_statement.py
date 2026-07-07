# continue transfers control to the beginning of the loop. 
# It skips the rest of the code inside the loop for the 
# current iteration only. 
# Loop does not terminate but continues on with the 
# next iteration.
# print 1 to 10 and skip 5 and 7
i=1
while i<=10:
    if i==5 or i==7:
        i=i+1
        continue
    print(i)
    i=i+1

