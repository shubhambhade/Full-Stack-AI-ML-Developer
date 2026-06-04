import time
def countdown(num):
    print("count down starting......")
    while num > 0:
        yield num
        num -= 1

g = countdown(10)

for value in g:
    print(value)
    time.sleep(1)