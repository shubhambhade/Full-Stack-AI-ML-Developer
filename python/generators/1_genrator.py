def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g = mygen()
print(type(g))

#first value
print(next(g))
#second value
print(next(g))
#third value
print(next(g))