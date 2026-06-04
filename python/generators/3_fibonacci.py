def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

for n in fib():
    if n > 100:
        break
    print(n)