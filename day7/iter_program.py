def myGenerator() :
    print( 'First item')
    yield 10
    print( ' Second item' )
    yield 20
    print( 'Last item')
    yield 30


l1=[4,22,6,2,7,33]
it=iter(l1)

print(next(it))

print(next(it))

gen=myGenerator()
print(next(gen))
print(next(gen))
