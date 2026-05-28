from multipledispatch import dispatch

@dispatch(int,int)
def add(first,second):
    result = first + second
    print(result)
@dispatch(int,float,int)
def add(first,second,third):
    result = first + second+third
    print(result)

add(10,20)
add(10,20.30,40)