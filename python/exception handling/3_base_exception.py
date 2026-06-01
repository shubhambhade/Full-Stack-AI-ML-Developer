try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print("The result : ",num1/num2)

except BaseException as msg:
    print('Exception Type : ',type(msg))
    print("The type of Exception : ",msg.__class__)
    print('Exception class name : ', msg.__class__.__name__)
    print('The Deecription of exception : ',msg)