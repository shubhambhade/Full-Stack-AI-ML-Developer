try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print("The result : ",num1/num2)

except ZeroDivisionError:
    print("cannot divide with zero")

except ValueError:
    print('please provide int values only')