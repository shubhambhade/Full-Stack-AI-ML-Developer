try:
    print(10/0)
except ZeroDivisionError as msg:
    print('Exception Type : ',type(msg))
    print("The type of Exception : ",msg.__class__)
    print('Exception class name : ', msg.__class__.__name__)
    print('The Deecription of exception : ',msg)
