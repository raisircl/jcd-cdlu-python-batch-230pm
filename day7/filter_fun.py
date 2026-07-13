def isprime(num):
    i=2
    while i<num:
        if num%i==0:
            break
        i+=1
    if num==i:
        return True
    else:
        return False


l1=[4,22,6,2,7,33]

l2=list(filter(isprime,l1))

print(l2)
